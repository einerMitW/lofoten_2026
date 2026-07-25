# API Router Authentication

**Summary**: REST-Endpunkte für Admin-Anmeldung, Session-Verifizierung und JWT-Token-Ausstellung.

**Sources**: [[backend/routers/auth.py]]

**Last updated**: 2026-07-25

---

Der `router_auth` verarbeitet Anmelde-Anfragen für den geschützten Administrationsbereich.

## Endpunkte

### `POST /api/auth/login`
Empfängt `username` und `password`. Bei erfolgreicher Validierung mittels [[crud_auth]] wird ein signierter JSON Web Token (JWT) generiert und im Response-Body sowie als Cookie zurückgegeben.

### `GET /api/auth/verify`
Überprüft das mitgeschickte Bearer Token und bestätigt, ob die Admin-Sitzung valide ist.

## Related pages
- [[crud_auth]]
- [[backend_config]]
- [[component_admin_login]]
