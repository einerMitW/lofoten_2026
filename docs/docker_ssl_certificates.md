# Docker SSL Certificates

**Summary**: Verwaltung von TLS/SSL-Zertifikaten und Einbindung in den Nginx-Container.

**Sources**: [[nginx/certs/generate-self-signed.sh]], [[docker-compose.yml]]

**Last updated**: 2026-07-25

---

Die Komponente `docker_ssl_certificates` regelt die TLS-Verschlüsselung der Webanwendung.

## Zertifikatseinbindung

- **Host-Verzeichnis**: `./nginx/certs/` beinhaltet `fullchain.pem` und `privkey.pem`.
- **Container Mount**: Wird schreibgeschützt nach `/etc/nginx/certs:ro` in den Frontend-Container gemountet.
- **Entwicklungs-Skript**: `generate-self-signed.sh` erzeugt bei Bedarf selbstsignierte Zertifikate mittels OpenSSL.

## Related pages
- [[docker_frontend_nginx]]
- [[docker_compose_orchestration]]
