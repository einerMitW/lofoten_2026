# Table Route Points

**Summary**: Datenmodell und Datenbankschema für geparste GPX-Trackpoints zur Visualisierung von Pfaden und Höhenprofilen.

**Sources**: [[backend/database.py]]

**Last updated**: 2026-07-25

---

Die Tabelle `route_points` speichert geordnete Koordinatenpunkte einer Wandertour, die aus hochgeladenen GPX-Dateien extrahiert werden.

## Schema-Struktur

| Feld | Typ | Beschreibung |
| :--- | :--- | :--- |
| `id` | INTEGER | Primärschlüssel (Auto-Increment) |
| `lat` | REAL | Breitengrad (Latitude) |
| `lon` | REAL | Längengrad (Longitude) |
| `elevation` | REAL | Höhe über dem Meeresspiegel in Metern |
| `cumulative_distance` | REAL | Kumulierte Distanz ab Startpunkt in Kilometern |
| `stage_index` | INTEGER | Zuordnungs-Index der GPX-Etappe |

## Nutzung im System
Die Daten bilden die Grundlage für die Polyline-Routendarstellung in der Kartenkomponente sowie für das interaktive Höhenprofil.

## Related pages
- [[database_engine]]
- [[crud_route_points]]
- [[router_gpx]]
- [[gpx_parser_core]]
- [[component_map_view]]
- [[component_elevation_profile]]
