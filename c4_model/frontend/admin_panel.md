# AdminPanel

| Eigenschaft | Wert |
|:---|:---|
| **Name** | AdminPanel |
| **Container** | Frontend (Vue.js) |
| **Sprache** | JavaScript / Vue.js SFC |

## Aufgabe
Zeigt die Karte im Admin-Modus an. Der Admin kann durch Klick auf die Karte einen neuen Wegpunkt platzieren. Der Klick öffnet den [ImageUpload](image_upload.md)-Dialog, über den ein Bild und eine Kurzbeschreibung für diesen Punkt hochgeladen werden können. Nur erreichbar nach erfolgreichem Login über [AdminLogin](admin_login.md).

## Begründung
Die Trennung von Admin- und User-Ansicht stellt sicher, dass normale Besucher die Karte nicht versehentlich verändern können. Der Admin benötigt eine eigene Ansicht, in der Klick-Events auf der Karte als "Wegpunkt platzieren" interpretiert werden und nicht als Navigation.

**User Story Bezug:** UC-5 (Bilder als Wegpunkt hochladen)

## Abhängigkeiten
- **Intern:**
  - Nutzt die Map-Instanz von → [MapView](map_view.md)
  - Nur erreichbar nach Login über → [AdminLogin](admin_login.md)
  - Öffnet bei Klick → [ImageUpload](image_upload.md)
  - Wegpunkt-Daten werden gespeichert über → [ApiClient](api_client.md) → [WaypointRouter](../backend/waypoint_router.md)
