# MapView

| Eigenschaft | Wert |
|:---|:---|
| **Name** | MapView |
| **Container** | Frontend (Vue.js) |
| **Sprache** | JavaScript / Vue.js SFC |

## Aufgabe
Initialisiert die Mapbox GL JS Karteninstanz und stellt den zentralen Karten-Canvas bereit, auf dem alle weiteren Layer (Route, Wegpunkte) gerendert werden. Verwaltet den Karten-Viewport (Zoom, Center, Pitch) und stellt die Map-Instanz als Provide/Inject-Kontext für Kind-Komponenten bereit.

## Begründung
Ohne die Karte gibt es keine Anwendung. MapView ist die **kritischste Komponente** des gesamten Frontends. Sie kapselt die gesamte Mapbox-Initialisierung und stellt sicher, dass der API-Token korrekt geladen und die Karte responsiv gerendert wird.

**User Story Bezug:** UC-1 (Karte mit Route sehen), UC-7 (Onepager-Layout)

## Abhängigkeiten
- **Extern:** Mapbox GL JS SDK, Mapbox Access Token
- **Intern:**
  - Stellt die Map-Instanz bereit für → [RouteLayer](route_layer.md)
  - Stellt die Map-Instanz bereit für → [WaypointMarker](waypoint_marker.md)
  - Stellt die Map-Instanz bereit für → [AdminPanel](admin_panel.md)
