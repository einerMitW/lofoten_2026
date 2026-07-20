# DatabaseManager

| Eigenschaft | Wert |
|:---|:---|
| **Name** | DatabaseManager |
| **Container** | Backend (FastAPI) |
| **Sprache** | Python |

## Aufgabe
Verwaltet die SQLite-Datenbankverbindung und stellt eine saubere Abstraktionsschicht für alle Datenbankoperationen bereit:
1. **Initialisierung:** Erstellt die SQLite-Datei (`data.db`) und legt das [Schema](../database/schema.md) (Tabellen) beim ersten Start automatisch an.
2. **Connection Management:** Stellt eine FastAPI-Dependency bereit (`get_db`), die eine Datenbankverbindung per Request öffnet und nach dem Request sauber schließt.
3. **Query-Abstraktion:** Kapselt SQL-Queries für CRUD-Operationen auf Wegpunkten.

### Sicherheit
- **Prepared Statements:** Alle Queries verwenden parametrisierte Statements (`?`-Platzhalter), um SQL-Injection zu verhindern.
- **Keine direkte Übernahme** von User-Eingaben in Query-Strings (vgl. developer_dialog.md, Abschnitt 7).

## Begründung
Eine zentrale Datenbankschicht sorgt für:
- **Konsistenz:** Alle Komponenten nutzen die gleiche Verbindungslogik.
- **Testbarkeit:** Die DB kann in Tests durch eine In-Memory-SQLite-Instanz ersetzt werden.
- **Wartbarkeit:** Schema-Änderungen finden an genau einer Stelle statt.

**User Story Bezug:** UC-6 (persistente Speicherung)

## Abhängigkeiten
- **Intern:**
  - Wird genutzt von → [WaypointRouter](waypoint_router.md)
  - Erstellt und verwaltet → [Schema](../database/schema.md)
- **Libraries:** `sqlite3` (Python Standard Library) oder `aiosqlite` (für async)
