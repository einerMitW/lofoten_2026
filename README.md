# Lofoten 2026 – Web Application

Eine moderne Webanwendung zur Aufbereitung, Routenplanung und interaktiven Erkundung der Lofoten-Fernwanderung 2026.

---

## Dokumentationsübersicht

Sämtliche Detaildokumentationen sind im Ordner [docs/](docs/index.md) als strukturierter Wissensgraph abgelegt. Die Hauptthemen finden Sie unter folgenden Links:

* [Kurzbeschreibung des Projektes](docs/project_overview.md) – Übersicht zu Funktionen, Kartendarstellung und Etappen-Handling.
* [Setup (manuell & docker)](docs/setup_guide.md) – Schritt-für-Schritt Einrichtung für lokale Entwickler und Docker.
* [Start der Anwendung (manuell & docker)](docs/getting_started.md) – Startbefehle für Frontend, Backend, Docker Compose und Test-Runner.
* [API Endpunkte](docs/api_endpoints.md) – Tabellarische Übersicht aller REST-Endpunkte mit Methoden und Beschreibungen.
* [Netzwerk für Deployment](docs/deployment_network.md) – Dokumentation der Docker-Bridge, Host-Loopback-Bindings (127.0.0.1:5567) und Reverse-Proxy-Integration.

---

## Kurzbeschreibung

Die Anwendung visualisiert den Verlauf der Lofoten-Durchquerung von Moskenesøya nach Austvågøya. Sie kombiniert eine interaktive Leaflet-Karte im Arctic-Dark-Design mit einem Chart.js Höhenprofil und synchronisiertem Laser-Scrubber. Über das integrierte Administrationsinterface können Wegepunkte und Tourenfotos hochgeladen und verwaltet werden.

Weitere Details finden Sie in der [Kurzbeschreibung des Projektes](docs/project_overview.md).

---

## Schnelleinstieg

### Docker Compose (Empfohlen)

```bash
# 1. Umgebungsvariablen anlegen
cp .env.example .env

# 2. Container im Hintergrund bauen und starten
docker-compose up --build -d
```
Die Anwendung ist anschließend lokal unter **http://127.0.0.1:5567** erreichbar.

Weitere Optionen finden Sie im [Setup Guide](docs/setup_guide.md) und in der [Startanleitung](docs/getting_started.md).

---

## REST API Schnellübersicht

Eine vollständige Tabelle aller Schnittstellen finden Sie unter [API Endpunkte](docs/api_endpoints.md).

| Methode | API | Funktionsbeschreibung |
| :--- | :--- | :--- |
| `GET` | `/` | Root-Healthcheck; bestätigt die Betriebsbereitschaft des Backends. |
| `GET` | `/api/route` | Ruft die zusammengefügten GPX-Routendaten und das Höhenprofil-Telemetry-JSON ab. |
| `GET` | `/api/waypoints` | Gibt eine Liste aller gespeicherten Wegepunkte (POIs) zurück. |
| `POST` | `/api/waypoints` | Erstellt einen neuen Wegepunkt (Admin Bearer Token erforderlich). |
| `DELETE` | `/api/waypoints/{id}` | Löscht den Wegepunkt mit der angegebenen ID (Admin Bearer Token erforderlich). |
| `GET` | `/api/images` | Gibt die Liste aller gespeicherten Bild-Metadaten zurück. |
| `POST` | `/api/images` | Lädt ein neues Bild hoch und speichert es in `ImageStorage` (Admin Bearer Token erforderlich). |
| `GET` | `/api/images/{filename}` | Serviert die Bilddatei des angegebenen Dateinamens. |
| `POST` | `/api/auth/login` | Authentifiziert den Administrator und gibt ein JWT Access Token zurück. |
| `GET` | `/api/auth/verify` | Prüft die Gültigkeit des übergebenen JWT Access Tokens. |

---

## Tests Ausführen

```bash
# Backend Tests (Pytest)
cd backend && python -m pytest

# Frontend Tests (Vitest)
cd frontend && npm run test
```
