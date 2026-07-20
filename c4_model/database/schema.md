# Schema (SQLite)

| Eigenschaft | Wert |
|:---|:---|
| **Name** | Schema |
| **Container** | Datenbank (SQLite) |
| **Sprache** | SQL |

## Aufgabe
Definiert das Datenbankschema der SQLite-Datenbank (`data.db`). Die Datenbank speichert ausschließlich **Metadaten**, keine Binärdaten (Bilder). Bilder liegen im [ImageStorage](../filesystem/image_storage.md).

## Tabelle: `waypoints`

| Spalte | Typ | Beschreibung |
|:---|:---|:---|
| `id` | `INTEGER PRIMARY KEY AUTOINCREMENT` | Eindeutige ID des Wegpunkts. |
| `latitude` | `REAL NOT NULL` | Breitengrad (WGS84). |
| `longitude` | `REAL NOT NULL` | Längengrad (WGS84). |
| `description` | `TEXT NOT NULL` | Kurzbeschreibung des Wegpunkts. |
| `image_path` | `TEXT NOT NULL` | Relativer Pfad zur Bilddatei im [ImageStorage](../filesystem/image_storage.md) (Pointer, kein BLOB). |
| `created_at` | `TEXT DEFAULT CURRENT_TIMESTAMP` | Erstellungszeitpunkt. |

```sql
CREATE TABLE IF NOT EXISTS waypoints (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    latitude    REAL    NOT NULL,
    longitude   REAL    NOT NULL,
    description TEXT    NOT NULL,
    image_path  TEXT    NOT NULL,
    created_at  TEXT    DEFAULT CURRENT_TIMESTAMP
);
```

## Begründung
- **SQLite** wurde gewählt, weil die Anwendung nur 2–10 Nutzer hat und die Datenmenge gering ist. SQLite braucht keinen separaten DB-Server und speichert alles in einer einzigen Datei.
- **Bilder als Pointer (`image_path`):** Bilder werden nicht als BLOB in der DB gespeichert, sondern im Dateisystem abgelegt. Der `image_path` ist ein relativer Pfad (z.B. `uploads/images/uuid4.jpg`), der als Referenz dient. Das hält die DB-Datei klein und die Bildauslieferung performant.

**User Story Bezug:** UC-6 (persistente Speicherung)

## Abhängigkeiten
- **Intern:**
  - Wird erstellt und verwaltet von → [DatabaseManager](../backend/database_manager.md)
  - `image_path` verweist auf Dateien in → [ImageStorage](../filesystem/image_storage.md)
  - Wird abgefragt von → [WaypointRouter](../backend/waypoint_router.md)
