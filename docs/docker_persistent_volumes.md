# Docker Persistent Volumes

**Summary**: Konfiguration von Docker Named Volumes für die dauerhafte Speicherung von Anwendungsdaten.

**Sources**: [[docker-compose.yml]]

**Last updated**: 2026-07-25

---

Die Komponente `docker_persistent_volumes` verhindert Datenverlust bei Container-Neustarts oder Image-Updates.

## Volume-Struktur

- `lofoten_db_data`: Sichere Speicherung der SQLite-Datenbank `data.db`.
- `lofoten_image_storage`: Speichert hochgeladene Standortfotos im Ordner `/app/ImageStorage`.
- `lofoten_gpx_storage`: Speichert hochgeladene GPX-Trackdateien im Ordner `/app/GpxStorage`.

## Related pages
- [[docker_compose_orchestration]]
- [[database_engine]]
- [[table_images]]
