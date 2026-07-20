# WaypointRouter

| Eigenschaft | Wert |
|:---|:---|
| **Name** | WaypointRouter |
| **Container** | Backend (FastAPI) |
| **Sprache** | Python |

## Aufgabe
FastAPI Router, der REST-Endpunkte für die Wegpunkt-Verwaltung bereitstellt:

| Methode | Endpunkt | Auth | Beschreibung |
|:---|:---|:---|:---|
| `GET` | `/api/waypoints` | Nein | Alle Wegpunkte abrufen (Koordinaten, Beschreibung, Bild-URL). |
| `POST` | `/api/waypoints` | Ja (Admin) | Neuen Wegpunkt mit Bild und Beschreibung anlegen. |
| `DELETE` | `/api/waypoints/{id}` | Ja (Admin) | Wegpunkt und zugehöriges Bild löschen. |

## Begründung
Wegpunkte sind die Brücke zwischen der Route und den Bildern. Das CRUD-Management dieser Entität muss serverseitig stattfinden, damit:
1. Nur authentifizierte Admins Daten verändern können.
2. Die Datenintegrität (Koordinaten, Bildpfad, Beschreibung) gewährleistet ist.
3. Die Eingaben durch den [InputSanitizer](input_sanitizer.md) bereinigt werden können.

**User Story Bezug:** UC-3 (Bilder anzeigen), UC-5 (Bilder hochladen), UC-6 (persistente Speicherung)

## Abhängigkeiten
- **Intern:**
  - Nutzt → [DatabaseManager](database_manager.md) für SQL-Queries
  - Delegiert Bild-Speicherung an → [ImageRouter](image_router.md)
  - Validiert Eingaben über → [InputSanitizer](input_sanitizer.md)
  - Prüft Admin-Berechtigung über → [AuthRouter](auth_router.md) (Dependency Injection)
  - Wird aufgerufen von → [ApiClient](../frontend/api_client.md) (Frontend)
