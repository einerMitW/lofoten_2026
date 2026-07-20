# ImageUpload

| Eigenschaft | Wert |
|:---|:---|
| **Name** | ImageUpload |
| **Container** | Frontend (Vue.js) |
| **Sprache** | JavaScript / Vue.js SFC |

## Aufgabe
Modaler Dialog (gleiche Glassmorphism-Optik wie [ImagePopup](image_popup.md)) in dem der Admin:
1. Ein Bild per Datei-Auswahl hochladen kann.
2. Eine Kurzbeschreibung eingeben kann.
3. Die Eingaben über den [ApiClient](api_client.md) an das Backend senden kann.

Die Koordinaten des neuen Wegpunktes werden vom [AdminPanel](admin_panel.md) übergeben (aus dem Klick-Event auf der Karte).

## Begründung
Der Upload-Dialog trennt die Datei- und Beschreibungseingabe von der Karteninteraktion. Er stellt sicher, dass der Admin alle nötigen Daten (Bild + Text) gesammelt übermitteln kann, bevor der Wegpunkt persistent gespeichert wird.

**User Story Bezug:** UC-5 (Bilder hochladen), UC-6 (persistente Speicherung)

## Abhängigkeiten
- **Intern:**
  - Wird geöffnet von → [AdminPanel](admin_panel.md)
  - Teilt UI-Komponente mit → [ImagePopup](image_popup.md) (gleiche Popup-Basis)
  - Sendet Upload über → [ApiClient](api_client.md)
  - Backend-Verarbeitung in → [ImageRouter](../backend/image_router.md)
  - Wegpunkt-Erstellung in → [WaypointRouter](../backend/waypoint_router.md)
