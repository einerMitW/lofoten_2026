# Containerization Docker Architecture

**Summary**: Multi-Container Orchestrierung der Lofoten 2026 Webanwendung mittels Docker, Nginx SSL und FastAPI.

**Sources**: [[docker-compose.yml]], [[frontend/Dockerfile]], [[backend/Dockerfile]], [[frontend/nginx.conf]]

**Last updated**: 2026-07-25

---

Die Komponente `containerization_docker` kapselt die Bereitstellung der Anwendung in zwei isolierten Docker-Containern.

## Architektur

### Frontend Container (`lofoten_frontend`)
- Multi-Stage Build: Node.js 20 zur Kompilierung der Vue 3 SPA und Nginx (alpine-slim) zur Bereitstellung der statischen Dateien.
- HTTPS-Endpunkt: Lauscht intern auf Port 443 mit SSL/TLS.
- Host-Port Mapping: Mapped Host-Port **5567** auf Container-Port 443 (`5567:443`).
- SSL-Zertifikate: Mountet `./nginx/certs` schreibgeschützt nach `/etc/nginx/certs:ro`.

### Backend Container (`lofoten_backend`)
- Python 3.11-slim Container mit FastAPI und Uvicorn.
- Isoliertes Netzwerk: Lauscht intern auf Port 8000 ohne direkten externen Host-Port.
- Persistenz: Named Volumes `lofoten_db_data`, `lofoten_image_storage` und `lofoten_gpx_storage`.

## Related pages
- [[backend_main]]
- [[frontend_main]]
- [[c4_architecture_model]]
- [[ci_backend_pipeline]]
- [[ci_frontend_pipeline]]
