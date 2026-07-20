# ImagePopup

| Eigenschaft | Wert |
|:---|:---|
| **Name** | ImagePopup |
| **Container** | Frontend (Vue.js) |
| **Sprache** | JavaScript / Vue.js SFC + Vanilla CSS |

## Aufgabe
Zeigt ein modales Overlay mit einem Bild und dessen Kurzbeschreibung an. Der Hintergrund wird mit einem Blur-Effekt (CSS `backdrop-filter`) abgedunkelt. Das Popup kann durch Klick auf den Hintergrund oder eine Schließen-Schaltfläche geschlossen werden.

Wird sowohl im **Anwender-Modus** (Bild betrachten) als auch im **Admin-Modus** (Vorschau nach Upload) verwendet.

## Begründung
Das Popup ist die zentrale Darstellungskomponente für die Urlaubsbilder. Es entkoppelt die Bilddarstellung von der Karte und bietet einen fokussierten, ästhetischen Rahmen für die Bilder – das Kernziel der gesamten Anwendung.

**User Story Bezug:** UC-3 (Bilder-Popup öffnen), UC-7 (minimalistisches UI)

## Abhängigkeiten
- **Intern:**
  - Wird geöffnet von → [WaypointMarker](waypoint_marker.md)
  - Wird wiederverwendet in → [ImageUpload](image_upload.md) (Admin-Vorschau)
  - Bild-URL wird vom Backend geliefert über → [ImageRouter](../backend/image_router.md)
