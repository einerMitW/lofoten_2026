# CRUD Operations Images

**Summary**: Datenbankschicht-Funktionen zum Verwalten von Bild-Datensätzen und deren Verknüpfungen.

**Sources**: [[backend/database.py]]

**Last updated**: 2026-07-25

---

Die Komponente `crud_images` verwaltet Datenbankzugriffe für hochgeladene Standortfotos.

## Kernfunktionen

- `get_all_images(db)`: Gibt eine Liste aller registrierten Bilder samt Pfaden und Koordinaten zurück.
- `create_image(db, image_data)`: Erstellt einen neuen Bildeintrag in der Datenbank.
- `delete_image(db, image_id)`: Löscht den Datenbankeintrag eines Bildes.

## Related pages
- [[table_images]]
- [[router_images]]
- [[database_engine]]
