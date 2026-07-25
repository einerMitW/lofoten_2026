# Frontend Router

**Summary**: Vue Router Routing-Konfiguration für die Navigation zwischen Kartenansicht und Administration.

**Sources**: [[frontend/src/router/index.js]]

**Last updated**: 2026-07-25

---

Die Komponente `frontend_router` verwaltet die Client-seitige Navigation der Vue SPA.

## Routen-Definitionen

- `/`: Lädt [[view_home]] (Interaktive Karte & Höhenprofil).
- `/admin`: Lädt [[view_admin]] (Dashboard für GPX- und Fotomanagement).

## History Mode
Verwendet `createWebHistory()`, um saubere URLs ohne Hash-Fragmente (`#`) im Browser zu ermöglichen.

## Related pages
- [[frontend_main]]
- [[view_home]]
- [[view_admin]]
