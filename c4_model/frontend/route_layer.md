# RouteLayer

| Eigenschaft | Wert |
|:---|:---|
| **Name** | RouteLayer |
| **Container** | Frontend (Vue.js) |
| **Sprache** | JavaScript / Vue.js SFC |

## Aufgabe
Empfängt die vom Backend gelieferten GPX-Daten (bereits in GeoJSON konvertiert) und zeichnet die Wanderroute als Linie auf der Mapbox-Karte. Steuert Styling der Linie (Farbe, Breite, Transparenz) und passt den Karten-Viewport so an, dass die gesamte Route sichtbar ist (`fitBounds`).

## Begründung
Die Route ist das Herzstück der Anwendung und der primäre visuelle Anker. Ohne die gezeichnete Route auf der Karte hat der Anwender keinen Kontext für die platzierten Bilder. Die Route ist ein MVP-Kernfeature.

**User Story Bezug:** UC-1 (Route auf der Karte sehen)

## Abhängigkeiten
- **Intern:**
  - Benötigt die Map-Instanz von → [MapView](map_view.md)
  - Ruft GeoJSON-Daten ab über → [ApiClient](api_client.md)
  - Die GeoJSON-Daten werden im Backend erzeugt von → [GpxParser](../backend/gpx_parser.md)
  - Liefert Höhendaten an → [ElevationProfile](elevation_profile.md)
