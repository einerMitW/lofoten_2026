# View Admin

**Summary**: Hauptansicht des Administrationsbereichs zur Verwaltung von GPX-Tracks, Bildern und Wegepunkten.

**Sources**: [[frontend/src/views/AdminView.vue]]

**Last updated**: 2026-07-25

---

Die Komponente `view_admin` dient als Kontrollzentrum für den Administrator.

## Enthaltene Komponenten & Funktionen

- [[component_admin_login]]: Wird angezeigt, wenn kein gültiger Admin-Token vorhanden ist.
- GPX-Upload-Bereich: Erlaubt das Hochladen neuer GPX-Etappen oder das Zurücksetzen des Routenverlaufs.
- Wegepunkt-Verwaltung: Erfassen, Bearbeiten und Löschen von POIs.
- [[component_image_upload]]: Upload und Verwaltung von Tourfotos.

## Related pages
- [[component_admin_login]]
- [[component_image_upload]]
- [[api_service]]
