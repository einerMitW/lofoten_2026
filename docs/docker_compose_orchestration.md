# Docker Compose Orchestration

**Summary**: Zentrale Orchestrierung der Multi-Container-Anwendung, Netzwerk-Isolation und Service-Abhängigkeiten.

**Sources**: [[docker-compose.yml]]

**Last updated**: 2026-07-25

---

Die Komponente `docker_compose_orchestration` steuert das Ausführen und Verknüpfen der einzelnen Anwendungs-Container.

## Service-Struktur

### Backend Service (`backend`)
- Baut auf [[docker_backend_container]] auf.
- Verknüpft Umgebungsvariablen für Admin-Passwort und Secret Key.
- Bindet persisente Volumes über [[docker_persistent_volumes]] ein.

### Frontend Service (`frontend`)
- Baut auf [[docker_frontend_nginx]] auf.
- Exponiert den öffentlichen Host-Port 5567 (HTTPS).
- Hängt über `depends_on` vom Backend-Service ab.

### Netzwerk (`lofoten_net`)
Definiert das isolierte Bridge-Netzwerk, über das Frontend und Backend gesichert untereinander kommunizieren.

## Related pages
- [[docker_frontend_nginx]]
- [[docker_backend_container]]
- [[docker_persistent_volumes]]
- [[c4_architecture_model]]
