# Table Users

**Summary**: Datenmodell und Datenbankschema für Administrator-Benutzerkonto und Passwort-Hashes.

**Sources**: [[backend/database.py]]

**Last updated**: 2026-07-25

---

Die Tabelle `users` speichert die Anmeldeinformationen für den Administrationsbereich der Anwendung.

## Schema-Struktur

| Feld | Typ | Beschreibung |
| :--- | :--- | :--- |
| `id` | INTEGER | Primärschlüssel (Auto-Increment) |
| `username` | TEXT | Eindeutiger Benutzername (Unique Index) |
| `hashed_password` | TEXT | Gehashter Passwort-String (Bcrypt / Passlib) |

## Nutzung im System
Das Schema wird ausschließlich während des Authentifizierungsprozesses verwendet, um eingehende Anmeldedaten zu prüfen und JWT-Tokens für geschützte API-Routen auszustellen.

## Related pages
- [[database_engine]]
- [[crud_auth]]
- [[router_auth]]
