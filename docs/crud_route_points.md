# CRUD Operations Route Points

**Summary**: Datenbankschicht-Funktionen zum Speichern, Abrufen und Zurücksetzen von GPX-Trackpoints.

**Sources**: [[backend/database.py]]

**Last updated**: 2026-07-25

---

Die Komponente `crud_route_points` verwaltet Datenbankzugriffe für geparste GPX-Routendaten.

## Kernfunktionen

- `get_all_route_points(db)`: Gibt die geordneten Trackpoints sortiert nach `stage_index` und `cumulative_distance` zurück.
- `bulk_insert_route_points(db, points)`: Führt ein performantes Bulk-Insert für Hunderte bis Tausende von Routenpunkten durch.
- `clear_route_points(db)`: Löscht alle bestehenden Routenpunkte vor dem Import eines neuen GPX-Tracks.

## Related pages
- [[table_route_points]]
- [[router_gpx]]
- [[gpx_parser_core]]
