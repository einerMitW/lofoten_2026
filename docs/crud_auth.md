# CRUD Operations Authentication

**Summary**: Funktionen für Benutzer-Lookup, Passwort-Verifizierung und Initialisierung von Admin-Zugängen.

**Sources**: [[backend/database.py]]

**Last updated**: 2026-07-25

---

Die Komponente `crud_auth` steuert die Sicherheits- und Benutzerabfragen auf Datenbankebene.

## Kernfunktionen

- `get_user_by_username(db, username)`: Lädt den Benutzer-Datensatz anhand des Benutzernamens.
- `verify_password(plain_password, hashed_password)`: Gleicht ein Klartext-Passwort mit dem abgespeicherten Hash ab.
- `hash_password(password)`: Generiert einen sicheren Hash für Passwörter.

## Related pages
- [[table_users]]
- [[router_auth]]
- [[backend_config]]
