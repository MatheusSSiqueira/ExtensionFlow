<div align="center">

# 🎓 ExtensionFlow

**Sistema RAG multi-agente para orientação de atividades extensionistas universitárias**

<a href="https://python.org"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMTAiIGhlaWdodD0iMjAiPjxyZWN0IHdpZHRoPSIxMTAiIGhlaWdodD0iMjAiIHJ4PSIzIiBmaWxsPSIjNGE1NTY4Ii8+PHJlY3QgeD0iNTgiIHdpZHRoPSI1MiIgaGVpZ2h0PSIyMCIgcng9IjMiIGZpbGw9IiMzNzc2QUIiLz48cmVjdCB4PSI1NSIgd2lkdGg9IjMiIGhlaWdodD0iMjAiIGZpbGw9IiMzNzc2QUIiLz48dGV4dCB4PSIyOSIgeT0iMTQiIGZpbGw9IiNmZmYiIGZvbnQtZmFtaWx5PSJEZWphVnUgU2FucyxWZXJkYW5hLEdlbmV2YSxzYW5zLXNlcmlmIiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5QeXRob248L3RleHQ+PHRleHQgeD0iODQiIHk9IjE0IiBmaWxsPSIjZmZmIiBmb250LWZhbWlseT0iRGVqYVZ1IFNhbnMsVmVyZGFuYSxHZW5ldmEsc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+My4xMSs8L3RleHQ+PC9zdmc+" alt="Python"/></a> <a href="https://langchain.com"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjQiIGhlaWdodD0iMjAiPjxyZWN0IHdpZHRoPSIxMjQiIGhlaWdodD0iMjAiIHJ4PSIzIiBmaWxsPSIjNGE1NTY4Ii8+PHJlY3QgeD0iNzkiIHdpZHRoPSI0NSIgaGVpZ2h0PSIyMCIgcng9IjMiIGZpbGw9IiMxYTdmNmUiLz48cmVjdCB4PSI3NiIgd2lkdGg9IjMiIGhlaWdodD0iMjAiIGZpbGw9IiMxYTdmNmUiLz48dGV4dCB4PSIzOSIgeT0iMTQiIGZpbGw9IiNmZmYiIGZvbnQtZmFtaWx5PSJEZWphVnUgU2FucyxWZXJkYW5hLEdlbmV2YSxzYW5zLXNlcmlmIiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5MYW5nQ2hhaW48L3RleHQ+PHRleHQgeD0iMTAxIiB5PSIxNCIgZmlsbD0iI2ZmZiIgZm9udC1mYW1pbHk9IkRlamFWdSBTYW5zLFZlcmRhbmEsR2VuZXZhLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPjAuMys8L3RleHQ+PC9zdmc+" alt="LangChain"/></a> <a href="https://faiss.ai"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNTgiIGhlaWdodD0iMjAiPjxyZWN0IHdpZHRoPSIxNTgiIGhlaWdodD0iMjAiIHJ4PSIzIiBmaWxsPSIjNGE1NTY4Ii8+PHJlY3QgeD0iNTIiIHdpZHRoPSIxMDYiIGhlaWdodD0iMjAiIHJ4PSIzIiBmaWxsPSIjMDA2NEQyIi8+PHJlY3QgeD0iNDkiIHdpZHRoPSIzIiBoZWlnaHQ9IjIwIiBmaWxsPSIjMDA2NEQyIi8+PHRleHQgeD0iMjYiIHk9IjE0IiBmaWxsPSIjZmZmIiBmb250LWZhbWlseT0iRGVqYVZ1IFNhbnMsVmVyZGFuYSxHZW5ldmEsc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+RkFJU1M8L3RleHQ+PHRleHQgeD0iMTA1IiB5PSIxNCIgZmlsbD0iI2ZmZiIgZm9udC1mYW1pbHk9IkRlamFWdSBTYW5zLFZlcmRhbmEsR2VuZXZhLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPlZlY3RvciBTZWFyY2g8L3RleHQ+PC9zdmc+" alt="FAISS"/></a> <a href="https://gradio.app"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMzciIGhlaWdodD0iMjAiPjxyZWN0IHdpZHRoPSIxMzciIGhlaWdodD0iMjAiIHJ4PSIzIiBmaWxsPSIjNGE1NTY4Ii8+PHJlY3QgeD0iNTgiIHdpZHRoPSI3OSIgaGVpZ2h0PSIyMCIgcng9IjMiIGZpbGw9IiNlMDdiMDAiLz48cmVjdCB4PSI1NSIgd2lkdGg9IjMiIGhlaWdodD0iMjAiIGZpbGw9IiNlMDdiMDAiLz48dGV4dCB4PSIyOSIgeT0iMTQiIGZpbGw9IiNmZmYiIGZvbnQtZmFtaWx5PSJEZWphVnUgU2FucyxWZXJkYW5hLEdlbmV2YSxzYW5zLXNlcmlmIiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5HcmFkaW88L3RleHQ+PHRleHQgeD0iOTciIHk9IjE0IiBmaWxsPSIjZmZmIiBmb250LWZhbWlseT0iRGVqYVZ1IFNhbnMsVmVyZGFuYSxHZW5ldmEsc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+SW50ZXJmYWNlPC90ZXh0Pjwvc3ZnPg==" alt="Gradio"/></a> <a href="https://bandit.readthedocs.io"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMzAiIGhlaWdodD0iMjAiPjxyZWN0IHdpZHRoPSIxMzAiIGhlaWdodD0iMjAiIHJ4PSIzIiBmaWxsPSIjNGE1NTY4Ii8+PHJlY3QgeD0iNTgiIHdpZHRoPSI3MiIgaGVpZ2h0PSIyMCIgcng9IjMiIGZpbGw9IiMyZTdkMzIiLz48cmVjdCB4PSI1NSIgd2lkdGg9IjMiIGhlaWdodD0iMjAiIGZpbGw9IiMyZTdkMzIiLz48dGV4dCB4PSIyOSIgeT0iMTQiIGZpbGw9IiNmZmYiIGZvbnQtZmFtaWx5PSJEZWphVnUgU2FucyxWZXJkYW5hLEdlbmV2YSxzYW5zLXNlcmlmIiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5CYW5kaXQ8L3RleHQ+PHRleHQgeD0iOTQiIHk9IjE0IiBmaWxsPSIjZmZmIiBmb250LWZhbWlseT0iRGVqYVZ1IFNhbnMsVmVyZGFuYSxHZW5ldmEsc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+MCBpc3N1ZXM8L3RleHQ+PC9zdmc+" alt="Bandit"/></a> <a href="https://pylint.org"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNDQiIGhlaWdodD0iMjAiPjxyZWN0IHdpZHRoPSIxNDQiIGhlaWdodD0iMjAiIHJ4PSIzIiBmaWxsPSIjNGE1NTY4Ii8+PHJlY3QgeD0iNTgiIHdpZHRoPSI4NiIgaGVpZ2h0PSIyMCIgcng9IjMiIGZpbGw9IiMyZTdkMzIiLz48cmVjdCB4PSI1NSIgd2lkdGg9IjMiIGhlaWdodD0iMjAiIGZpbGw9IiMyZTdkMzIiLz48dGV4dCB4PSIyOSIgeT0iMTQiIGZpbGw9IiNmZmYiIGZvbnQtZmFtaWx5PSJEZWphVnUgU2FucyxWZXJkYW5hLEdlbmV2YSxzYW5zLXNlcmlmIiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5QeWxpbnQ8L3RleHQ+PHRleHQgeD0iMTAxIiB5PSIxNCIgZmlsbD0iI2ZmZiIgZm9udC1mYW1pbHk9IkRlamFWdSBTYW5zLFZlcmRhbmEsR2VuZXZhLHNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEiIHRleHQtYW5jaG9yPSJtaWRkbGUiPjEwLjAwIC8gMTA8L3RleHQ+PC9zdmc+" alt="Pylint"/></a> <a href="LICENSE"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNTEiIGhlaWdodD0iMjAiPjxyZWN0IHdpZHRoPSIxNTEiIGhlaWdodD0iMjAiIHJ4PSIzIiBmaWxsPSIjNGE1NTY4Ii8+PHJlY3QgeD0iNjUiIHdpZHRoPSI4NiIgaGVpZ2h0PSIyMCIgcng9IjMiIGZpbGw9IiMxNTY1YzAiLz48cmVjdCB4PSI2MiIgd2lkdGg9IjMiIGhlaWdodD0iMjAiIGZpbGw9IiMxNTY1YzAiLz48dGV4dCB4PSIzMiIgeT0iMTQiIGZpbGw9IiNmZmYiIGZvbnQtZmFtaWx5PSJEZWphVnUgU2FucyxWZXJkYW5hLEdlbmV2YSxzYW5zLXNlcmlmIiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5MaWNlbnNlPC90ZXh0Pjx0ZXh0IHg9IjEwOCIgeT0iMTQiIGZpbGw9IiNmZmYiIGZvbnQtZmFtaWx5PSJEZWphVnUgU2FucyxWZXJkYW5hLEdlbmV2YSxzYW5zLXNlcmlmIiBmb250LXNpemU9IjExIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5BcGFjaGUgMi4wPC90ZXh0Pjwvc3ZnPg==" alt="License"/></a>

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3ODAgMzAwIiB3aWR0aD0iNzgwIiBoZWlnaHQ9IjMwMCIgZm9udC1mYW1pbHk9IidTZWdvZSBVSScsc3lzdGVtLXVpLHNhbnMtc2VyaWYiPgogIDxyZWN0IHdpZHRoPSI3ODAiIGhlaWdodD0iMzAwIiByeD0iMTIiIGZpbGw9IiMwZjE3MmEiLz4KICA8dGV4dCB4PSIzOTAiIHk9IjI4IiBmaWxsPSIjOTRhM2I4IiBmb250LXNpemU9IjEyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBsZXR0ZXItc3BhY2luZz0iMiI+RVhURU5TSU9ORkxPVyDigJQgQVJRVUlURVRVUkE8L3RleHQ+CiAgPHJlY3QgeD0iMjAiIHk9IjQ0IiB3aWR0aD0iMTYwIiBoZWlnaHQ9IjIzMCIgcng9IjgiIGZpbGw9IiMxZTI5M2IiIHN0cm9rZT0iIzMzNDE1NSIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KICA8dGV4dCB4PSIxMDAiIHk9IjY0IiBmaWxsPSIjNjQ3NDhiIiBmb250LXNpemU9IjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGxldHRlci1zcGFjaW5nPSIxIj5JTlRFUkZBQ0U8L3RleHQ+CiAgPHRleHQgeD0iMTAwIiB5PSI4MCIgZmlsbD0iI2UyZThmMCIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjYwMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+YXBwLnB5PC90ZXh0PgogIDxyZWN0IHg9IjM2IiB5PSI5MCIgd2lkdGg9IjEyOCIgaGVpZ2h0PSIyMiIgcng9IjQiIGZpbGw9IiMwZjE3MmEiLz48dGV4dCB4PSIxMDAiIHk9IjEwNSIgZmlsbD0iIzdkZDNmYyIgZm9udC1zaXplPSIxMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+R3JhZGlvIENoYXQgVUk8L3RleHQ+CiAgPHJlY3QgeD0iMzYiIHk9IjExOCIgd2lkdGg9IjEyOCIgaGVpZ2h0PSIyMiIgcng9IjQiIGZpbGw9IiMwZjE3MmEiLz48dGV4dCB4PSIxMDAiIHk9IjEzMyIgZmlsbD0iIzdkZDNmYyIgZm9udC1zaXplPSIxMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+UHJvdmlkZXIgU2VsZWN0b3I8L3RleHQ+CiAgPHJlY3QgeD0iMzYiIHk9IjE0NiIgd2lkdGg9IjEyOCIgaGVpZ2h0PSIyMiIgcng9IjQiIGZpbGw9IiMwZjE3MmEiLz48dGV4dCB4PSIxMDAiIHk9IjE2MSIgZmlsbD0iIzdkZDNmYyIgZm9udC1zaXplPSIxMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+Q3Vyc28gSW5wdXQ8L3RleHQ+CiAgPHJlY3QgeD0iMzYiIHk9IjE3NCIgd2lkdGg9IjEyOCIgaGVpZ2h0PSIyMiIgcng9IjQiIGZpbGw9IiMwZjE3MmEiLz48dGV4dCB4PSIxMDAiIHk9IjE4OSIgZmlsbD0iIzdkZDNmYyIgZm9udC1zaXplPSIxMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+TWVtb3J5IExvZ2dlcjwvdGV4dD4KICA8cmVjdCB4PSIzNiIgeT0iMjAyIiB3aWR0aD0iMTI4IiBoZWlnaHQ9IjIyIiByeD0iNCIgZmlsbD0iIzBmMTcyYSIvPjx0ZXh0IHg9IjEwMCIgeT0iMjE3IiBmaWxsPSIjN2RkM2ZjIiBmb250LXNpemU9IjEwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5fQWdlbnRTdGF0ZTwvdGV4dD4KICA8cmVjdCB4PSIzNiIgeT0iMjMwIiB3aWR0aD0iMTI4IiBoZWlnaHQ9IjIyIiByeD0iNCIgZmlsbD0iIzBmMTcyYSIvPjx0ZXh0IHg9IjEwMCIgeT0iMjQ1IiBmaWxsPSIjN2RkM2ZjIiBmb250LXNpemU9IjEwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5yZXNldCgpIC8gaXNfcmVhZHkoKTwvdGV4dD4KICA8cmVjdCB4PSIyMTAiIHk9IjQ0IiB3aWR0aD0iMTYwIiBoZWlnaHQ9IjIzMCIgcng9IjgiIGZpbGw9IiMxZTI5M2IiIHN0cm9rZT0iIzMzNDE1NSIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KICA8dGV4dCB4PSIyOTAiIHk9IjY0IiBmaWxsPSIjNjQ3NDhiIiBmb250LXNpemU9IjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGxldHRlci1zcGFjaW5nPSIxIj5BR0VOVEU8L3RleHQ+CiAgPHRleHQgeD0iMjkwIiB5PSI4MCIgZmlsbD0iI2UyZThmMCIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjYwMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+QXR0ZW5kYW50QWdlbnQ8L3RleHQ+CiAgPHJlY3QgeD0iMjI2IiB5PSI5MCIgd2lkdGg9IjEyOCIgaGVpZ2h0PSIyMiIgcng9IjQiIGZpbGw9IiMwZjE3MmEiLz48dGV4dCB4PSIyOTAiIHk9IjEwNSIgZmlsbD0iIzg2ZWZhYyIgZm9udC1zaXplPSIxMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+T2JzZXJ2ZTwvdGV4dD4KICA8cmVjdCB4PSIyMjYiIHk9IjExOCIgd2lkdGg9IjEyOCIgaGVpZ2h0PSIyMiIgcng9IjQiIGZpbGw9IiMwZjE3MmEiLz48dGV4dCB4PSIyOTAiIHk9IjEzMyIgZmlsbD0iIzg2ZWZhYyIgZm9udC1zaXplPSIxMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+UmVhc29uPC90ZXh0PgogIDxyZWN0IHg9IjIyNiIgeT0iMTQ2IiB3aWR0aD0iMTI4IiBoZWlnaHQ9IjIyIiByeD0iNCIgZmlsbD0iIzBmMTcyYSIvPjx0ZXh0IHg9IjI5MCIgeT0iMTYxIiBmaWxsPSIjODZlZmFjIiBmb250LXNpemU9IjEwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5BY3Q8L3RleHQ+CiAgPHJlY3QgeD0iMjI2IiB5PSIxNzQiIHdpZHRoPSIxMjgiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMGYxNzJhIi8+PHRleHQgeD0iMjkwIiB5PSIxODkiIGZpbGw9IiM4NmVmYWMiIGZvbnQtc2l6ZT0iMTAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPmhhbmRsZSgpPC90ZXh0PgogIDxyZWN0IHg9IjIyNiIgeT0iMjAyIiB3aWR0aD0iMTI4IiBoZWlnaHQ9IjIyIiByeD0iNCIgZmlsbD0iIzBmMTcyYSIvPjx0ZXh0IHg9IjI5MCIgeT0iMjE3IiBmaWxsPSIjODZlZmFjIiBmb250LXNpemU9IjEwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5sb2dfY29ycmVjdGlvbigpPC90ZXh0PgogIDxyZWN0IHg9IjIyNiIgeT0iMjMwIiB3aWR0aD0iMTI4IiBoZWlnaHQ9IjIyIiByeD0iNCIgZmlsbD0iIzBmMTcyYSIvPjx0ZXh0IHg9IjI5MCIgeT0iMjQ1IiBmaWxsPSIjODZlZmFjIiBmb250LXNpemU9IjEwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5MTE0gQ2hhaW48L3RleHQ+CiAgPHJlY3QgeD0iNDAwIiB5PSI0NCIgd2lkdGg9IjE2MCIgaGVpZ2h0PSIyMzAiIHJ4PSI4IiBmaWxsPSIjMWUyOTNiIiBzdHJva2U9IiMzMzQxNTUiIHN0cm9rZS13aWR0aD0iMS41Ii8+CiAgPHRleHQgeD0iNDgwIiB5PSI2NCIgZmlsbD0iIzY0NzQ4YiIgZm9udC1zaXplPSI5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBsZXR0ZXItc3BhY2luZz0iMSI+QUdFTlRFPC90ZXh0PgogIDx0ZXh0IHg9IjQ4MCIgeT0iODAiIGZpbGw9IiNlMmU4ZjAiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI2MDAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkFuYWx5c3RBZ2VudDwvdGV4dD4KICA8cmVjdCB4PSI0MTYiIHk9IjkwIiB3aWR0aD0iMTI4IiBoZWlnaHQ9IjIyIiByeD0iNCIgZmlsbD0iIzBmMTcyYSIvPjx0ZXh0IHg9IjQ4MCIgeT0iMTA1IiBmaWxsPSIjZmJiZjI0IiBmb250LXNpemU9IjEwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5hbmFseXplKCk8L3RleHQ+CiAgPHJlY3QgeD0iNDE2IiB5PSIxMTgiIHdpZHRoPSIxMjgiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMGYxNzJhIi8+PHRleHQgeD0iNDgwIiB5PSIxMzMiIGZpbGw9IiNmYmJmMjQiIGZvbnQtc2l6ZT0iMTAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPnVwZGF0ZV9tZW1vcnkoKTwvdGV4dD4KICA8cmVjdCB4PSI0MTYiIHk9IjE0NiIgd2lkdGg9IjEyOCIgaGVpZ2h0PSIyMiIgcng9IjQiIGZpbGw9IiMwZjE3MmEiLz48dGV4dCB4PSI0ODAiIHk9IjE2MSIgZmlsbD0iI2ZiYmYyNCIgZm9udC1zaXplPSIxMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+UHJvbXB0IEd1YXJkcmFpbHM8L3RleHQ+CiAgPHJlY3QgeD0iNDE2IiB5PSIxNzQiIHdpZHRoPSIxMjgiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMGYxNzJhIi8+PHRleHQgeD0iNDgwIiB5PSIxODkiIGZpbGw9IiNmYmJmMjQiIGZvbnQtc2l6ZT0iMTAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkxMTSBDaGFpbjwvdGV4dD4KICA8cmVjdCB4PSI0MTYiIHk9IjIwMiIgd2lkdGg9IjEyOCIgaGVpZ2h0PSIyMiIgcng9IjQiIGZpbGw9IiMwZjE3MmEiLz48dGV4dCB4PSI0ODAiIHk9IjIxNyIgZmlsbD0iI2ZiYmYyNCIgZm9udC1zaXplPSIxMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+X2Zvcm1hdF9kb2NzKCk8L3RleHQ+CiAgPHJlY3QgeD0iNDE2IiB5PSIyMzAiIHdpZHRoPSIxMjgiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMGYxNzJhIi8+PHRleHQgeD0iNDgwIiB5PSIyNDUiIGZpbGw9IiNmYmJmMjQiIGZvbnQtc2l6ZT0iMTAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkZBSVNTIFJldHJpZXZlcjwvdGV4dD4KICA8cmVjdCB4PSI1OTAiIHk9IjQ0IiB3aWR0aD0iMTcwIiBoZWlnaHQ9IjIzMCIgcng9IjgiIGZpbGw9IiMxZTI5M2IiIHN0cm9rZT0iIzMzNDE1NSIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KICA8dGV4dCB4PSI2NzUiIHk9IjY0IiBmaWxsPSIjNjQ3NDhiIiBmb250LXNpemU9IjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGxldHRlci1zcGFjaW5nPSIxIj5EQURPUzwvdGV4dD4KICA8dGV4dCB4PSI2NzUiIHk9IjgwIiBmaWxsPSIjZTJlOGYwIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNjAwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5Bcm1hemVuYW1lbnRvPC90ZXh0PgogIDxyZWN0IHg9IjYwNiIgeT0iOTAiIHdpZHRoPSIxMzgiIGhlaWdodD0iMzgiIHJ4PSI0IiBmaWxsPSIjMGYxNzJhIi8+PHRleHQgeD0iNjc1IiB5PSIxMDciIGZpbGw9IiNjMDg0ZmMiIGZvbnQtc2l6ZT0iMTAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPkZBSVNTIEluZGV4PC90ZXh0Pjx0ZXh0IHg9IjY3NSIgeT0iMTIxIiBmaWxsPSIjNjQ3NDhiIiBmb250LXNpemU9IjkiIHRleHQtYW5jaG9yPSJtaWRkbGUiPmVtYmVkZGluZ3MgKyB0b3AtSzwvdGV4dD4KICA8cmVjdCB4PSI2MDYiIHk9IjEzNCIgd2lkdGg9IjEzOCIgaGVpZ2h0PSIzOCIgcng9IjQiIGZpbGw9IiMwZjE3MmEiLz48dGV4dCB4PSI2NzUiIHk9IjE1MSIgZmlsbD0iI2MwODRmYyIgZm9udC1zaXplPSIxMCIgdGV4dC1hbmNob3I9Im1pZGRsZSI+RE9DWCAvIFBERjwvdGV4dD48dGV4dCB4PSI2NzUiIHk9IjE2NSIgZmlsbD0iIzY0NzQ4YiIgZm9udC1zaXplPSI5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5kb2N1bWVudG9zIGluc3RpdHVjaW9uYWlzPC90ZXh0PgogIDxyZWN0IHg9IjYwNiIgeT0iMTc4IiB3aWR0aD0iMTM4IiBoZWlnaHQ9IjM4IiByeD0iNCIgZmlsbD0iIzBmMTcyYSIvPjx0ZXh0IHg9IjY3NSIgeT0iMTk1IiBmaWxsPSIjYzA4NGZjIiBmb250LXNpemU9IjEwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5yZWdyYXNfbWVtb3JpYS50eHQ8L3RleHQ+PHRleHQgeD0iNjc1IiB5PSIyMDkiIGZpbGw9IiM2NDc0OGIiIGZvbnQtc2l6ZT0iOSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+bWVtw7NyaWEgZGUgbG9uZ28gcHJhem88L3RleHQ+CiAgPHJlY3QgeD0iNjA2IiB5PSIyMjIiIHdpZHRoPSIxMzgiIGhlaWdodD0iMzgiIHJ4PSI0IiBmaWxsPSIjMGYxNzJhIi8+PHRleHQgeD0iNjc1IiB5PSIyMzkiIGZpbGw9IiNjMDg0ZmMiIGZvbnQtc2l6ZT0iMTAiIHRleHQtYW5jaG9yPSJtaWRkbGUiPi5lbnY8L3RleHQ+PHRleHQgeD0iNjc1IiB5PSIyNTMiIGZpbGw9IiM2NDc0OGIiIGZvbnQtc2l6ZT0iOSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+Y2hhdmVzIGRlIEFQSTwvdGV4dD4KICA8ZGVmcz48bWFya2VyIGlkPSJhIiBtYXJrZXJXaWR0aD0iOCIgbWFya2VySGVpZ2h0PSI4IiByZWZYPSI2IiByZWZZPSIzIiBvcmllbnQ9ImF1dG8iPjxwYXRoIGQ9Ik0wLDAgTDAsNiBMOCwzIHoiIGZpbGw9IiM0NzU1NjkiLz48L21hcmtlcj48L2RlZnM+CiAgPGxpbmUgeDE9IjE4MSIgeTE9IjE1OSIgeDI9IjIwOCIgeTI9IjE1OSIgc3Ryb2tlPSIjNDc1NTY5IiBzdHJva2Utd2lkdGg9IjEuNSIgbWFya2VyLWVuZD0idXJsKCNhKSIvPgogIDxsaW5lIHgxPSIzNzEiIHkxPSIxNTkiIHgyPSIzOTgiIHkyPSIxNTkiIHN0cm9rZT0iIzQ3NTU2OSIgc3Ryb2tlLXdpZHRoPSIxLjUiIG1hcmtlci1lbmQ9InVybCgjYSkiLz4KICA8bGluZSB4MT0iNTYxIiB5MT0iMTU5IiB4Mj0iNTg4IiB5Mj0iMTU5IiBzdHJva2U9IiM0NzU1NjkiIHN0cm9rZS13aWR0aD0iMS41IiBtYXJrZXItZW5kPSJ1cmwoI2EpIi8+CiAgPHRleHQgeD0iMzkwIiB5PSIyOTAiIGZpbGw9IiM0NzU1NjkiIGZvbnQtc2l6ZT0iOSIgdGV4dC1hbmNob3I9Im1pZGRsZSI+Z2l0aHViLmNvbS9NYXRoZXVzU1NpcXVlaXJhL2V4dGVuc2lvbmZsb3cgwrcgQXBhY2hlIDIuMDwvdGV4dD4KPC9zdmc+" alt="Arquitetura ExtensionFlow" width="100%"/>

</div>

---

## Sobre o projeto

O **ExtensionFlow** é um sistema de *Retrieval-Augmented Generation* (RAG) com dois agentes colaborativos, projetado para auxiliar alunos universitários a navegar nos requisitos das atividades extensionistas — sem precisar vasculhar manuais extensos.

O aluno faz sua pergunta em linguagem natural. O sistema busca nos documentos institucionais, extrai as regras relevantes e responde de forma estruturada, **sem inventar informações**.

> **Autor:** Matheus S. Siqueira · ADS · Unicesumar · [@MatheusSSiqueira](https://github.com/MatheusSSiqueira)

---

## Funcionalidades

| | Funcionalidade | Detalhe |
|:-:|:---|:---|
| 🔍 | **Busca semântica** | FAISS + embeddings — encontra por significado, não por palavra exata |
| 🤖 | **Workflow ReAct** | Observe → Reason → Act em dois agentes colaborativos |
| 🌐 | **3 provedores** | ChatGPT · Claude · Gemini — troca sem alterar código |
| 🔒 | **Segurança auditada** | Bandit 0 issues · Pylint 10/10 nos dois arquivos |
| 🛡️ | **Proteções de entrada** | Anti-prompt-injection · path traversal bloqueado |
| 💾 | **Memória persistente** | Regras aprendidas recarregadas automaticamente |
| 🖥️ | **Interface Gradio** | Chatbot visual · URL pública automática no Google Colab |
| 📄 | **Multi-formato** | Lê DOCX e PDF em uma só passagem |

---

## Fluxo ReAct

```
Aluno faz pergunta
      │
      ▼
AttendantAgent ── Observe
  └─ valida campos obrigatórios (curso)
  └─ sanitiza entrada (anti-injection, limite 2.000 chars)
      │
      ▼
ManualAnalystAgent ── Act
  └─ FAISS recupera top-4 chunks semanticamente relevantes
  └─ injeta regras da memória de longo prazo
      │
      ▼
ManualAnalystAgent ── Reason  (LLM)
  └─ extrai regras, prazos e requisitos dos chunks
  └─ cita o arquivo de origem de cada informação
  └─ nunca inventa dados ausentes  (guardrail no prompt)
      │
      ▼
AttendantAgent ── Reason + Act  (LLM)
  └─ refina em linguagem acessível ao aluno
  └─ organiza em passos numerados
  └─ adiciona template de lista de presença se necessário
      │
      ▼
Resposta estruturada → aluno
```

---

## Provedores de LLM

| Provedor | LLM | Embeddings | Variável |
|:---|:---|:---|:---|
| **ChatGPT** | GPT-4o | text-embedding-3-small | `OPENAI_API_KEY` |
| **Claude** | claude-sonnet-4-5 | text-embedding-3-small | `ANTHROPIC_API_KEY` |
| **Gemini** ✦ | gemini-1.5-pro | models/embedding-001 | `GOOGLE_API_KEY` |

> ✦ Gemini é o único provedor com embeddings **sem custo adicional** — ideal para projetos universitários com orçamento limitado.

---

## Instalação

**Pré-requisitos:** Python 3.11+ · chave de API de ao menos um provedor

```bash
# 1. Clonar
git clone https://github.com/MatheusSSiqueira/extensionflow.git
cd extensionflow

# 2. Instalar dependências
pip install langchain langchain-text-splitters langchain-core \
            langchain-openai langchain-anthropic \
            langchain-google-genai langchain-community \
            faiss-cpu pdfplumber python-docx tiktoken \
            gradio python-dotenv

# 3. Configurar .env
cp .env.example .env   # edite com sua chave de API
```

**Arquivo `.env`:**

```env
LLM_PROVIDER=openai          # openai | anthropic | gemini
OPENAI_API_KEY=sk-...
# ANTHROPIC_API_KEY=sk-ant-...
# GOOGLE_API_KEY=AIza...

CONTENT_DIR=/caminho/para/seus/documentos
FAISS_INDEX_PATH=/caminho/para/salvar/indice
```

**Documentos na pasta `CONTENT_DIR`:**

```
/content/
├── manual_extensao.docx
├── regulamento_atividades.pdf
└── guia_studeo.pdf
```

---

## Uso

```bash
# Interface visual (recomendado)
python app.py
# → http://localhost:7860  |  No Colab: URL pública automática

# Linha de comando
python extensionflow.py
```

**No Google Colab:**

```python
!pip install langchain langchain-openai langchain-community \
             faiss-cpu pdfplumber python-docx tiktoken gradio python-dotenv

from google.colab import files
files.upload()   # faça upload dos DOCX/PDF

!python app.py   # URL pública gerada automaticamente
```

---

## Segurança

Auditado com análise estática em resposta ao estudo da Fatec sobre vulnerabilidades em código gerado por IA.

| Ferramenta | `extensionflow.py` | `app.py` |
|:---|:---:|:---:|
| **Bandit** (OWASP) | ✅ 0 issues | ✅ 0 issues |
| **Pylint** | ✅ 10.00/10 | ✅ 10.00/10 |

**Proteções implementadas:**

| Categoria | Implementação |
|:---|:---|
| Chaves de API | Lidas de `.env` · nunca logadas · validadas por regex |
| Prompt Injection | `_sanitize_query()` — remove chars de controle, limite 2.000 chars |
| Path Traversal | `_safe_path()` — bloqueia arquivos fora de `CONTENT_DIR` |
| Allowlist | `_validate_provider()` com `frozenset` — bloqueia provedores não mapeados |
| Bind de rede | `127.0.0.1` local · `0.0.0.0` apenas no Colab (efêmero) |
| Exceções | Tipos específicos em vez de `except Exception` genérico |

---

## Estrutura do projeto

```
extensionflow/
├── extensionflow.py   # Backend: agentes, pipeline RAG, fábrica de LLM
├── app.py             # Interface Gradio + _AgentState singleton
├── .env.example       # Template de configuração
├── .gitignore         # Exclui .env, índice FAISS e chaves
├── README.md          # Este arquivo
└── LICENSE            # Apache License 2.0
```

---

## Roadmap

- [ ] Memória dinâmica — auto-gravação durante a conversa
- [ ] Integração com a API da plataforma Studeo
- [ ] Testes unitários com `pytest` (cobertura ≥ 80%)
- [ ] Deploy em Hugging Face Spaces

---

## Licença

Distribuído sob a **Apache License 2.0** — consulte [LICENSE](LICENSE).

---

<div align="center">
Desenvolvido por <strong>Matheus S. Siqueira</strong> · ADS · Unicesumar
</div>
