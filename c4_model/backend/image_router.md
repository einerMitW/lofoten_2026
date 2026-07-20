# ImageRouter

| Eigenschaft | Wert |
|:---|:---|
| **Name** | ImageRouter |
| **Container** | Backend (FastAPI) |
| **Sprache** | Python |

## Aufgabe
FastAPI Router, der Bild-Upload und -Auslieferung verwaltet:

| Methode | Endpunkt | Auth | Beschreibung |
|:---|:---|:---|:---|
| `POST` | `/api/images` | Ja (Admin) | Bild hochladen. Generiert UUID-Dateinamen, speichert die Datei im [ImageStorage](../filesystem/image_storage.md) und gibt den Dateipfad zurück. |
| `GET` | `/api/images/{filename}` | Nein | Einzelnes Bild ausliefern (Static File Response). |

### Upload-Ablauf
1. Admin sendet Bild als `multipart/form-data`.
2. ImageRouter prüft den MIME-Type (nur `image/jpeg`, `image/png`, `image/webp`).
3. Generiert einen eindeutigen Dateinamen (`uuid4.extension`).
4. Speichert die Datei physisch im [ImageStorage](../filesystem/image_storage.md)-Verzeichnis.
5. Gibt den relativen Pfad zurück, der als **Pointer** in der SQLite-Datenbank gespeichert wird.

## Begründung
Die Trennung von Bild-Upload und Wegpunkt-Erstellung erlaubt es, die Dateiverarbeitung (MIME-Check, UUID-Generierung, Speicherung) isoliert zu testen und zu warten. Das Backend ist der "Türsteher": Es kontrolliert, welche Dateitypen akzeptiert werden und verhindert die Ausführung bösartiger Dateien.

**User Story Bezug:** UC-5 (Bilder hochladen), UC-6 (persistente Speicherung)
**Abuse Case Bezug:** AC-2 (bösartige Dateien)

## Abhängigkeiten
- **Intern:**
  - Speichert Dateien in → [ImageStorage](../filesystem/image_storage.md)
  - Wird aufgerufen von → [WaypointRouter](waypoint_router.md) (bei Wegpunkt-Erstellung)
  - Validiert Eingaben über → [InputSanitizer](input_sanitizer.md)
  - Bild-URLs werden im Frontend angezeigt in → [ImagePopup](../frontend/image_popup.md)
