# Backend Main Application

**Summary**: FastAPI Hauptinstanz, Konfiguration der CORS-Middleware, Verzeichnis-Mounting für statische Dateien und Einbindung der API-Router.

**Sources**: [[backend/main.py]]

**Last updated**: 2026-07-25

---

Die Komponente `backend_main` stellt den zentralen Einstiegspunkt der Python Backend-Anwendung auf Basis des FastAPI-Frameworks dar.

## Funktionalität und Setup

### Anwendungs-Initialisierung
Die Instanz `app` wird als `FastAPI()` erzeugt. Sie dient als zentraler Anker für alle HTTP-Anfragen, Router und Middleware-Komponenten.

### CORS Middleware Configuration
Für die reibungslose Kommunikation zwischen dem Vue.js Frontend (standardmäßig auf Port 5173/3000) und dem FastAPI Backend wird die `CORSMiddleware` eingebunden. Dies erlaubt Cross-Origin-Requests für Entwicklungs- und Produktionsumgebungen.

### Statisches Dateiverzeichnis (`/static/images`)
Über `app.mount("/static/images", StaticFiles(directory=...))` werden hochgeladene Standortfotos direkt vom Dateisystem ausgeliefert. Die Pfadquelle wird dynamisch über [[backend_config]] bezogen.

### Router Registrierung
Die Anwendungslogik ist in modulare Router aufgeteilt, die mittels `app.include_router()` eingebunden werden:
- [[router_auth]] (`/api/auth`)
- [[router_gpx]] (`/api/gpx`)
- [[router_waypoints]] (`/api/waypoints`)
- [[router_images]] (`/api/images`)

## Related pages
- [[backend_config]]
- [[router_auth]]
- [[router_gpx]]
- [[router_waypoints]]
- [[router_images]]
