# -*- coding: utf-8 -*-
"""
ExtensionFlow — Interface Gradio
=================================
Interface de chat visual para interagir com os agentes do ExtensionFlow
diretamente no Google Colab ou em qualquer ambiente local.

Como executar no Colab:
    !python app.py

Como executar localmente:
    python app.py

Dependências adicionais:
    pip install gradio
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import logging
import threading
from typing import Optional

import gradio as gr

from extensionflow import (
    CONTENT_DIR,
    FAISS_INDEX_PATH,
    MEMORY_FILE,
    RETRIEVER_K,
    AttendantAgent,
    ManualAnalystAgent,
    _validate_provider,          # noqa: WPS437 — necessário para validação na UI
    append_to_memory,
    build_chunks,
    build_embeddings,
    build_llm,
    build_vectorstore,
    load_documents,
    load_memory_rules,
)

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Estado global dos agentes (singleton por módulo)
# ---------------------------------------------------------------------------

class _AgentState:
    """Contêiner do estado singleton dos agentes."""

    lock:      threading.Lock           = threading.Lock()
    attendant: Optional[AttendantAgent] = None
    config:    dict                     = {}

    def reset(self) -> None:
        """Reinicia o estado (desconecta os agentes ativos)."""
        with self.lock:
            self.attendant = None
            self.config    = {}
        log.info("AgentState: estado reiniciado.")

    def is_ready(self) -> bool:
        """Retorna True se os agentes estão inicializados e prontos."""
        return self.attendant is not None

_state = _AgentState()

# ---------------------------------------------------------------------------
# Mapeamento de provedores
# ---------------------------------------------------------------------------
PROVIDER_LABELS: dict[str, str] = {
    "ChatGPT (OpenAI)":   "openai",
    "Claude (Anthropic)": "anthropic",
    "Gemini (Google)":    "gemini",
}

KEY_PLACEHOLDERS: dict[str, str] = {
    "ChatGPT (OpenAI)":   "sk-...",
    "Claude (Anthropic)": "sk-ant-...",
    "Gemini (Google)":    "AIza...",
}

# ---------------------------------------------------------------------------
# Lógica de negócio da interface
# ---------------------------------------------------------------------------

def _init_agents(provider_label: str, api_key: str, _curso: str) -> str:
    """
    Inicializa (ou reinicializa) os agentes com o provedor e chave informados.
    Retorna mensagem de status formatada em Markdown.
    """

    provider = PROVIDER_LABELS.get(provider_label, "")
    try:
        provider = _validate_provider(provider)
    except ValueError as exc:
        return f"❌ {exc}"

    cfg = {"provider": provider}
    if cfg == _state.config and _state.is_ready():
        return "✅ Agentes já ativos com essa configuração."

    try:
        docs = load_documents(CONTENT_DIR)
        if not docs:
            return (
                f"⚠️ Nenhum documento encontrado em `{CONTENT_DIR}`.\n\n"
                "Faça o upload dos arquivos DOCX/PDF para esse diretório e tente novamente."
            )

        chunk_list  = build_chunks(docs)
        embeddings  = build_embeddings(provider, api_key)
        vector_store = build_vectorstore(chunk_list, FAISS_INDEX_PATH, embeddings)
        retriever   = vector_store.as_retriever(search_kwargs={"k": RETRIEVER_K})
        llm         = build_llm(provider, api_key)
        memory      = load_memory_rules(MEMORY_FILE)

        analyst    = ManualAnalystAgent(retriever=retriever, llm=llm, memory_rules=memory)
        new_agent  = AttendantAgent(analyst=analyst, llm=llm)

        with _state.lock:
            _state.attendant  = new_agent
            _state.config     = cfg

        return (
            f"✅ **ExtensionFlow ativo!**\n\n"
            f"• Provedor : **{provider_label}**\n"
            f"• Documentos: **{len(docs)}**\n"
            f"• Chunks   : **{len(chunk_list)}**\n\n"
            "Faça sua pergunta no chat ao lado. 👉"
        )

    except EnvironmentError as exc:
        return f"🔑 Erro de chave de API:\n\n`{exc}`"
    except (ValueError, RuntimeError) as exc:
        return f"❌ Erro ao inicializar:\n\n`{exc}`"


def _respond(message: str, history: list, curso: str) -> tuple[list, str]:
    """Processa uma mensagem do aluno e retorna histórico atualizado."""
    if not message.strip():
        return history, ""

    if not _state.is_ready():
        reply = (
            "⚠️ Agentes não inicializados.\n"
            "Configure o provedor e a chave no painel esquerdo e clique em **Conectar**."
        )
        return history + [[message, reply]], ""

    if not curso.strip():
        reply = (
            "Para te ajudar, preciso saber: **qual é o seu curso?**\n"
            "Preencha o campo no painel esquerdo."
        )
        return history + [[message, reply]], ""

    with _state.lock:
        reply = _state.attendant.handle(
            student_query=message,
            context={"curso": curso.strip()},
        )

    return history + [[message, reply]], ""


def _save_correction(correction: str) -> str:
    """Salva uma correção/regra na memória do agente."""
    if not correction.strip():
        return "⚠️ Digite a correção antes de salvar."
    append_to_memory(correction)
    return "✅ Regra salva na memória."


def _update_placeholder(provider_label: str):
    """Atualiza o placeholder do campo de chave conforme o provedor."""
    return gr.update(placeholder=KEY_PLACEHOLDERS.get(provider_label, "..."))


# ---------------------------------------------------------------------------
# Construção da interface Gradio
# ---------------------------------------------------------------------------

CSS = """
#ef-title  { font-size: 1.9rem; font-weight: 700; margin-bottom: 0; }
#ef-sub    { color: #6b7280; margin-top: 2px; font-size: 0.88rem; }
#status-md { font-size: 0.84rem; line-height: 1.55; }
footer     { display: none !important; }
"""

EXAMPLES = [
    "Qual é o prazo para envio da atividade de extensão?",
    "Qual o formato exigido para o relatório?",
    "Como faço o upload no Studeo?",
    "Preciso de lista de presença? Como preencher?",
    "Quais documentos devo anexar na submissão?",
]


def build_interface() -> gr.Blocks:
    """Constrói e retorna o objeto gr.Blocks da interface ExtensionFlow."""

    with gr.Blocks(
        title="ExtensionFlow",
        theme=gr.themes.Soft(primary_hue="blue", neutral_hue="slate"),
        css=CSS,
    ) as demo:

        # ── Cabeçalho ──────────────────────────────────────────────────
        gr.Markdown("# 🎓 ExtensionFlow", elem_id="ef-title")
        gr.Markdown(
            "Assistente RAG para dúvidas sobre atividades extensionistas · "
            "Powered by LLM + FAISS",
            elem_id="ef-sub",
        )

        with gr.Row(equal_height=False):

            # ── Painel esquerdo — Configuração ──────────────────────────
            with gr.Column(scale=1, min_width=290):
                gr.Markdown("### ⚙️ Configuração")

                provider_radio = gr.Radio(
                    choices=list(PROVIDER_LABELS.keys()),
                    value="ChatGPT (OpenAI)",
                    label="Provedor de IA",
                )
                api_key_box = gr.Textbox(
                    label="Chave de API",
                    placeholder="sk-...",
                    type="password",
                    info="Nunca salva nem registrada em logs.",
                )
                curso_box = gr.Textbox(
                    label="Seu curso",
                    placeholder="Ex.: Análise e Desenvolvimento de Sistemas",
                    info="Necessário para contextualizar as respostas.",
                )
                connect_btn = gr.Button("🔌 Conectar", variant="primary")
                status_md   = gr.Markdown(
                    "Configure o provedor e clique em **Conectar** para começar.",
                    elem_id="status-md",
                )

                gr.Markdown("---")
                gr.Markdown("### 📝 Reportar correção")
                correction_box = gr.Textbox(
                    label="Regra ou correção",
                    placeholder="Ex.: O prazo para ADS é sempre a última sexta do mês.",
                    lines=2,
                )
                save_btn        = gr.Button("💾 Salvar na memória")
                correction_msg  = gr.Markdown("")

            # ── Painel direito — Chat ──────────────────────────────────
            with gr.Column(scale=3):
                gr.Markdown("### 💬 Chat")

                chatbot = gr.Chatbot(
                    label="ExtensionFlow",
                    height=500,
                    bubble_full_width=False,
                    show_copy_button=True,
                    avatar_images=(
                        "https://api.dicebear.com/7.x/thumbs/svg?seed=aluno",
                        "https://api.dicebear.com/7.x/thumbs/svg?seed=extensionflow",
                    ),
                )

                with gr.Row():
                    msg_box  = gr.Textbox(
                        placeholder="Digite sua dúvida sobre a atividade de extensão...",
                        label="",
                        scale=5,
                        container=False,
                    )
                    send_btn = gr.Button("Enviar ➤", variant="primary", scale=1)

                clear_btn = gr.Button("🗑️ Limpar conversa", size="sm", variant="secondary")

                gr.Examples(
                    examples=EXAMPLES,
                    inputs=msg_box,
                    label="💡 Perguntas frequentes",
                )

        # ── Eventos ────────────────────────────────────────────────────

        provider_radio.change(
            fn=_update_placeholder,
            inputs=provider_radio,
            outputs=api_key_box,
        )

        connect_btn.click(
            fn=_init_agents,
            inputs=[provider_radio, api_key_box, curso_box],
            outputs=status_md,
        )

        send_btn.click(
            fn=_respond,
            inputs=[msg_box, chatbot, curso_box],
            outputs=[chatbot, msg_box],
        )
        msg_box.submit(
            fn=_respond,
            inputs=[msg_box, chatbot, curso_box],
            outputs=[chatbot, msg_box],
        )

        clear_btn.click(fn=lambda: [], outputs=chatbot)

        save_btn.click(
            fn=_save_correction,
            inputs=correction_box,
            outputs=correction_msg,
        )

    return demo


# ---------------------------------------------------------------------------
# Execução
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        import google.colab  # pylint: disable=unused-import
        IN_COLAB = True
    except ImportError:
        IN_COLAB = False

    interface = build_interface()
    interface.launch(
        share=IN_COLAB,
        inbrowser=not IN_COLAB,
        server_name=("0.0.0.0" if IN_COLAB else "127.0.0.1"),  # nosec B104
        server_port=7860,
        show_error=True,
    )
