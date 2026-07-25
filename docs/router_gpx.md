# API Router GPX

**Summary**: REST-Endpunkte zum Hochladen von GPX-Dateien und Bereitstellen geparster Routenpunkte.

**Sources**: [[backend/routers/gpx.py]]

**Last updated**: 2026-07-25

---

Der `router_gpx` stellt die Schnittstellen für die Routenverarbeitung bereit.

## Endpunkte

### `POST /api/gpx/upload`
Geschützter Endpunkt (Admin-Token erforderlich). Empfängt eine oder mehrere `.gpx` Dateien, übergibt diese an [[gpx_parser_core]] und speichert die bereinigten Punkte in [[table_route_points]].

### `GET /api/gpx/route`
Öffentlicher Endpunkt. Liefert alle verarbeiteten Trackpoints geordnet nach Distanz und Etappe zur Visualisierung auf Karte und Höhenprofil.

## Related pages
- [[gpx_parser_core]]
- [[crud_route_points]]
- [[component_map_view]]
- [[component_elevation_profile]]
