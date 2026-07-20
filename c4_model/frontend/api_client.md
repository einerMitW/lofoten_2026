# ApiClient

| Eigenschaft | Wert |
|:---|:---|
| **Name** | ApiClient |
| **Container** | Frontend (Vue.js) |
| **Sprache** | JavaScript (ES Module) |

## Aufgabe
Zentraler HTTP-Client-Service, der alle REST-API-Aufrufe an das FastAPI-Backend bündelt. Kapselt `fetch()`-Aufrufe, setzt den Auth-Token im Header (nach Login), verarbeitet Fehler einheitlich und stellt typisierte Methoden bereit:

- `getRoute()` → GeoJSON der Route laden
- `getWaypoints()` → Alle Wegpunkte abrufen
- `login(password)` → Admin authentifizieren
- `createWaypoint(lat, lng, image, description)` → Neuen Wegpunkt mit Bild anlegen
- `deleteWaypoint(id)` → Wegpunkt entfernen

## Begründung
Ohne eine zentrale Abstraktionsschicht für API-Aufrufe würde jede Komponente ihre eigene `fetch()`-Logik implementieren. Das führt zu Duplikation, inkonsistenter Fehlerbehandlung und erschwerter Wartung. Der ApiClient ist der **einzige Punkt** im Frontend, der die Backend-URL kennt.

**Prinzip:** Single Responsibility, DRY (Don't Repeat Yourself)

## Abhängigkeiten
- **Intern:**
  - Wird verwendet von → [RouteLayer](route_layer.md)
  - Wird verwendet von → [WaypointMarker](waypoint_marker.md)
  - Wird verwendet von → [AdminLogin](admin_login.md)
  - Wird verwendet von → [ImageUpload](image_upload.md)
- **Extern:**
  - Kommuniziert mit dem Backend über HTTP → [GpxParser](../backend/gpx_parser.md), [WaypointRouter](../backend/waypoint_router.md), [ImageRouter](../backend/image_router.md), [AuthRouter](../backend/auth_router.md)
