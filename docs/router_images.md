# API Router Images

**Summary**: REST-Endpunkte für den Upload, Abruf und das Löschen von Standortfotos.

**Sources**: [[backend/routers/images.py]]

**Last updated**: 2026-07-25

---

Der `router_images` verwaltet den Bildertransfer zwischen Client und Server.

## Endpunkte

### `GET /api/images`
Öffentlich. Gibt Metadaten aller hochgeladenen Bilder inklusive statischer Bild-URLs zurück.

### `POST /api/images/upload`
Geschützt. Nimmt Bilddateien entgegen, speichert diese im Dateisystem unter `IMAGE_DIR` und legt den Eintrags-Record über [[crud_images]] an.

### `DELETE /api/images/{id}`
Geschützt. Löscht die Bilddatei vom Dateisystem und entfernt den Datensatz aus der Datenbank.

## Related pages
- [[crud_images]]
- [[table_images]]
- [[backend_config]]
- [[component_image_upload]]
- [[component_image_popup]]
