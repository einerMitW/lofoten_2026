# API Router Waypoints

**Summary**: REST-Endpunkte für CRUD-Operationen an geographischen Wegepunkten.

**Sources**: [[backend/routers/waypoints.py]]

**Last updated**: 2026-07-25

---

Der `router_waypoints` ermöglicht das Erfassen und Abrufen von Point-of-Interest Datensätzen.

## Endpunkte

### `GET /api/waypoints`
Öffentlicher Endpunkt. Gibt die Liste aller gespeicherten Wegepunkte als JSON zurück.

### `POST /api/waypoints`
Geschützt. Erstellt einen neuen Wegepunkt nach Sanitisierung mittels [[sanitizer]].

### `PUT /api/waypoints/{id}`
Geschützt. Aktualisiert die Daten eines bestehenden Wegepunkts.

### `DELETE /api/waypoints/{id}`
Geschützt. Entfernt einen Wegepunkt aus der Datenbank.

## Related pages
- [[crud_waypoints]]
- [[table_waypoints]]
- [[sanitizer]]
- [[component_map_view]]
