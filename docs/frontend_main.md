# Frontend Main Application

**Summary**: Vue 3 Anwendungsinstanz, Einbindung des Routers und globales CSS-Styling-Setup.

**Sources**: [[frontend/src/main.js]], [[frontend/src/App.vue]], [[frontend/src/style.css]]

**Last updated**: 2026-07-25

---

Die Komponente `frontend_main` initialisiert die Single Page Application (SPA) auf Basis von Vue 3 und Vite.

## Aufbau

### App-Mounting (`main.js`)
Erzeugt die Vue-App mittels `createApp(App)`, bindet den [[frontend_router]] ein und mountet die Anwendung in den HTML-DOM (`#app`).

### Haupt-Layout (`App.vue`)
Stellt die Kopfzeile mit Anwendungs-Titel und Navigation zwischen Kartenansicht (`/`) und Admin-Dashboard (`/admin`) bereit. Verwaltet globale Events.

### Styling (`style.css`)
Beinhaltet das dunkle Farbschema (Modern Dark Mode) sowie globale Reset- und Schriftart-Regeln.

## Related pages
- [[frontend_router]]
- [[view_home]]
- [[view_admin]]
