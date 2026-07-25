# API Endpoints

**Summary**: Übersicht aller REST-API Endpunkte des FastAPI Backends im Tabellenformat.

**Sources**: [[backend/main.py]], [[backend/routers/]]

**Last updated**: 2026-07-25

---

Sämtliche Endpunkte der Anwendung sind nachfolgend tabellarisch aufgeführt.

## REST-Schnittstellen Übersicht

| Methode | API | Funktionsbeschreibung |
| :--- | :--- | :--- |
| `GET` | `/` | Root-Healthcheck; bestätigt die Betriebsbereitschaft des Backends. |
| `GET` | `/api/route` | Ruft die geparsten GPX-Routendaten (GeoJSON) und Telemetriedaten für die Karte und das Höhenprofil ab. |
| `GET` | `/api/waypoints` | Gibt eine Liste aller gespeicherten Wegepunkte (Hütten, Gipfel, Zeltplätze) als JSON zurück. |
| `POST` | `/api/waypoints` | Erstellt einen neuen Wegepunkt mit Titel, Beschreibung, Koordinaten und Bild-Pfad (Admin Bearer Token erforderlich). |
| `DELETE` | `/api/waypoints/{id}` | Löscht den Wegepunkt mit der angegebenen ID aus der Datenbank (Admin Bearer Token erforderlich). |
| `GET` | `/api/images` | Gibt eine Liste aller registrierten Bild-Metadaten zurück. |
| `POST` | `/api/images` | Lädt eine Bilddatei hoch, speichert diese in `ImageStorage` und gibt die Bild-URL zurück (Admin Bearer Token erforderlich). |
| `GET` | `/api/images/{filename}` | Serviert die Bilddatei des angegebenen Dateinamens direkt aus dem Speicher. |
| `POST` | `/api/auth/login` | Authentifiziert den Administrator anhand des Passworts und gibt ein JWT Access Token zurück. |
| `GET` | `/api/auth/verify` | Prüft die Gültigkeit des übergebenen JWT Access Tokens. |

## Related pages
- [[router_auth]]
- [[router_gpx]]
- [[router_waypoints]]
- [[router_images]]
