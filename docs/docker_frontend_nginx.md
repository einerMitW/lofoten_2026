# Docker Frontend Nginx

**Summary**: Multi-Stage Container-Build für Vue 3 und Nginx SSL Reverse Proxy Konfiguration.

**Sources**: [[frontend/Dockerfile]], [[frontend/nginx.conf]], [[frontend/.dockerignore]]

**Last updated**: 2026-07-25

---

Die Komponente `docker_frontend_nginx` verwaltet die Erstellung und Bereitstellung der Frontend-Anwendung.

## Multi-Stage Build

1. **Stage 1 (Build)**: Nutzt `node:20-alpine`, führt `npm ci` aus und kompiliert die Vue 3 SPA nach `/app/dist`.
2. **Stage 2 (Production)**: Kopiert die kompilierte Dist nach `/usr/share/nginx/html` in ein schlankes `nginx:alpine-slim` Image.

## Nginx SSL & Proxy Konfiguration

- Lauscht auf Port `443` mit SSL/TLS.
- Terminiert TLS-Verschlüsselung über Zertifikate aus [[docker_ssl_certificates]].
- Proxy `location /api/` an `http://backend:8000/api/`.

## Related pages
- [[docker_compose_orchestration]]
- [[docker_ssl_certificates]]
- [[frontend_main]]
