# Database Engine & Connection

**Summary**: Verwaltung der SQLite-Datenbankverbindung, Session-Handling und Initialisierung von Schemas.

**Sources**: [[backend/database.py]]

**Last updated**: 2026-07-25

---

Die Komponente `database_engine` ist verantwortlich für die Anbindung an die SQLite-Datenbank `data.db` und die Verwaltung von Datenbank-Sessions.

## Verbindungsaufbau und Schema-Initialisierung

### SQLite Engine Configuration
Die Verbindung wird über SQLAlchemy / SQLite hergestellt. Da SQLite standardmäßig Thread-Verifizierungen durchführt, wird für den Multi-Thread-Betrieb mit FastAPI `check_same_thread=False` konfiguriert.

### Session Lifecycle (`get_db`)
Über den Generator `get_db()` stellt das Modul Abhängigkeiten (Dependencies) für FastAPI-Endpunkte bereit. Jede Anfrage erhält eine eigene Datenbank-Session, die nach Abschluss der Anfrage sauber geschlossen wird.

### Tabellen-Initialisierung (`init_db`)
Beim Start der Anwendung prüft `init_db()`, ob die erforderlichen Tabellen existieren, und legt diese bei Bedarf automatisch an:
- [[table_users]]
- [[table_waypoints]]
- [[table_route_points]]
- [[table_images]]

## Related pages
- [[table_users]]
- [[table_waypoints]]
- [[table_route_points]]
- [[table_images]]
- [[backend_config]]
