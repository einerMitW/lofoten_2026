# Table Images

**Summary**: Datenmodell und Datenbankschema für Bildreferenzen, Koordinaten und Metadaten.

**Sources**: [[backend/database.py]]

**Last updated**: 2026-07-25

---

Die Tabelle `images` verfaltet Metadaten hochgeladener Standort- und Tourenfotos.

## Schema-Struktur

| Feld | Typ | Beschreibung |
| :--- | :--- | :--- |
| `id` | INTEGER | Primärschlüssel (Auto-Increment) |
| `filename` | TEXT | Eindeutiger Dateiname im Dateisystem |
| `filepath` | TEXT | Relativer Pfad zum Bild |
| `title` | TEXT | Bildtitel / Beschreibung |
| `lat` | REAL | Breitengrad des Aufnahmeorts (optional) |
| `lon` | REAL | Längengrad des Aufnahmeorts (optional) |
| `waypoint_id` | INTEGER | Fremdschlüssel zu `waypoints.id` (optional) |
| `created_at` | TIMESTAMP | Erstellungs-Zeitstempel |

## Nutzung im System
Ermöglicht das Anzeigen von Fotomarkern auf der Karte sowie die Zuordnung von Bildern zu spezifischen Wegepunkten.

## Related pages
- [[database_engine]]
- [[crud_images]]
- [[router_images]]
- [[component_image_popup]]
