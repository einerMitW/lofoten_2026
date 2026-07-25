# Component Image Upload

**Summary**: Formularkomponente zum Hochladen neuer Standortfotos mit Koordinaten-Zuordnung.

**Sources**: [[frontend/src/components/ImageUpload.vue]]

**Last updated**: 2026-07-25

---

Die Komponente `component_image_upload` befindet sich im Admin-Dashboard.

## Funktionen

- Datei-Auswahl: Drag-and-Drop oder Dateidialog für `.jpg` und `.png` Dateien.
- Georeferenzierung: Eingabefelder für Breitengrad (`lat`) und Längengrad (`lon`) oder automatische Übernahme ausgewählter Wegepunkte.
- Übertragung: Sendet Multipart-FormData an [[router_images]].

## Related pages
- [[router_images]]
- [[view_admin]]
- [[api_service]]
