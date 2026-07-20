# WaypointMarker

| Eigenschaft | Wert |
|:---|:---|
| **Name** | WaypointMarker |
| **Container** | Frontend (Vue.js) |
| **Sprache** | JavaScript / Vue.js SFC |

## Aufgabe
Platziert für jeden Wegpunkt aus der Datenbank einen Marker auf der Mapbox-Karte an den entsprechenden Koordinaten. Reagiert auf Klick-Events und öffnet bei Klick das zugehörige [ImagePopup](image_popup.md) mit dem Bild und der Kurzbeschreibung.

## Begründung
Wegpunkte sind die Verbindung zwischen der Route und den Urlaubsbildern. Sie machen die Karte interaktiv und erzählen die Geschichte der Reise. Ohne Marker gäbe es keine Möglichkeit, Bilder im Kontext der Route zu erleben.

**User Story Bezug:** UC-3 (Bilder-Popup öffnen)

## Abhängigkeiten
- **Intern:**
  - Benötigt die Map-Instanz von → [MapView](map_view.md)
  - Lädt Wegpunkt-Daten über → [ApiClient](api_client.md)
  - Öffnet bei Klick → [ImagePopup](image_popup.md)
  - Wegpunkt-Daten kommen aus → [WaypointRouter](../backend/waypoint_router.md) (Backend)
