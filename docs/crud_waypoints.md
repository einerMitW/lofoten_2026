# CRUD Operations Waypoints

**Summary**: Datenbankschicht-Funktionen zum Erstellen, Lesen, Aktualisieren und Löschen von Wegepunkten.

**Sources**: [[backend/database.py]]

**Last updated**: 2026-07-25

---

Die Komponente `crud_waypoints` kapselt die SQL-Abfragen für die Tabelle [[table_waypoints]].

## Kernfunktionen

- `get_all_waypoints(db)`: Ruft sämtliche gespeicherten Wegepunkte ab.
- `create_waypoint(db, waypoint_data)`: Speichert einen neuen Wegepunkt ab.
- `update_waypoint(db, waypoint_id, data)`: Aktualisiert die Eigenschaften eines bestehenden Wegepunkts.
- `delete_waypoint(db, waypoint_id)`: Löscht den angegebenen Wegepunkt aus der Datenbank.

## Related pages
- [[table_waypoints]]
- [[router_waypoints]]
- [[database_engine]]
