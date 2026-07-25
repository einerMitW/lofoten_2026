# Docker Backend Container

**Summary**: Containerisierung der Python FastAPI Anwendung im isolierten Docker-Netzwerk.

**Sources**: [[backend/Dockerfile]], [[backend/.dockerignore]]

**Last updated**: 2026-07-25

---

Die Komponente `docker_backend_container` kapselt die Ausführung der FastAPI Backend-Logik.

## Container-Konfiguration

- Base Image: `python:3.11-slim` für minimale Image-Größe.
- Abhängigkeiten: Installiert `requirements.txt` ohne Pip-Cache (`--no-cache-dir`).
- Startbefehl: Startet `uvicorn main:app --host 0.0.0.0 --port 8000`.
- Netzwerk-Isolation: Kein direkter Host-Port gedoppelt; Erreichbarkeit nur über [[docker_compose_orchestration]] bridge.

## Related pages
- [[docker_compose_orchestration]]
- [[backend_main]]
- [[database_engine]]
