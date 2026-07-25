# Table Waypoints

**Summary**: Datenmodell und Datenbankschema für geographische Wegepunkte entlang der Wanderroute.

**Sources**: [[backend/database.py]]

**Last updated**: 2026-07-25

---

Die Tabelle `waypoints` speichert Point-of-Interest (POI) Informationen wie Hütten, Gipfel, Zeltplätze und Schlüsselstellen entlang der Lofoten-Route.

## Schema-Struktur

| Feld | Typ | Beschreibung |
| :--- | :--- | :--- |
| `id` | INTEGER | Primärschlüssel (Auto-Increment) |
| `name` | TEXT | Bezeichnung des Wegepunkts |
| `lat` | REAL | Breitengrad (Latitude in WGS84) |
| `lon` | REAL | Längengrad (Longitude in WGS84) |
| `description` | TEXT | Ausführliche Beschreibung / Hinweise |
| `category` | TEXT | Kategorie (z. B. Hütte, Camping, Wasser, Gipfel) |
| `stage_index` | INTEGER | Zuordnung zur jeweiligen Etappennummer |

## Nutzung im System
Wegepunkte werden über die API abgerufen und auf der Leaflet-Karte als Interaktive Marker dargestellt. Sie können im Admin-Panel verwaltet werden.

## Related pages
- [[database_engine]]
- [[crud_waypoints]]
- [[router_waypoints]]
- [[component_map_view]]
