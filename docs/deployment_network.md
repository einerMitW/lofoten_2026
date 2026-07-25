# Deployment Network Architecture

**Summary**: Dokumentation der Netzwerkstruktur, Portmappings (extern/intern) und TLS-Offloading.

**Sources**: [[docker-compose.yml]], [[frontend/nginx.conf]]

**Last updated**: 2026-07-25

---

Die Netzwerkarchitektur wurde für ein sicheres Deployment hinter einem übergeordneten SSL-Reverse-Proxy konzipiert.

## Portmapping Übersicht

| Komponente | Container-Port (Intern) | Host-Binding (Extern) | Protokoll | Erreichbarkeit |
| :--- | :--- | :--- | :--- | :--- |
| **Frontend (Nginx)** | `80` | `127.0.0.1:5567` | HTTP | Nur lokal vom Host-System (Proxy) |
| **Backend (FastAPI)** | `8000` | *Keines* | HTTP | Nur intern im `lofoten_net` |

## Sicherheits- und Netzwerkkonzept

### Loopback Binding (`127.0.0.1:5567`)
Durch das Binding an `127.0.0.1:5567:80` wird direkter externer Zugriff aus dem Internet auf den unverschlüsselten HTTP-Port blockiert. Nur der auf dem Host-System installierte Reverse Proxy (z. B. Nginx, Caddy, Traefik) kann Anfragen weiterleiten.

### Docker Bridge Network (`lofoten_net`)
Das Backend ist nicht an den Host gebunden. Der Frontend-Container kommuniziert isoliert über den Servicenamen `http://backend:8000` im virtuellen Bridge-Netzwerk.

## Related pages
- [[docker_compose_orchestration]]
- [[docker_frontend_nginx]]
- [[getting_started]]
