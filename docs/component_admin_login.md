# Component Admin Login

**Summary**: Anmeldeformular für den Administrationsbereich mit JWT Token Handling und LocalStorage-Speicherung.

**Sources**: [[frontend/src/components/AdminLogin.vue]]

**Last updated**: 2026-07-25

---

Die Komponente `component_admin_login` steuert den Zugang zum Admin-Dashboard.

## Ablauf

1. Formular-Eingabe: Erfasst Benutzername und Passwort.
2. Authentifizierungs-Request: Sendet Daten via [[api_service]] an [[router_auth]].
3. Token-Handling: Speichert den empfangenen JWT-Token im `localStorage` für nachfolgende geschützte API-Aufrufe.

## Related pages
- [[router_auth]]
- [[view_admin]]
- [[api_service]]
