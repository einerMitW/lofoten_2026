# Test Infrastructure Backend

**Summary**: Pytest-Testsuite Konfiguration, Fixtures für In-Memory SQLite Testdatenbanken und temporäre Ordnerisolation.

**Sources**: [[backend/tests/conftest.py]], [[backend/pytest.ini]]

**Last updated**: 2026-07-25

---

Die Komponente `test_infrastructure_backend` stellt eine saubere, isolierte Testumgebung für das FastAPI Backend bereit.

## Fixtures & Test-Isolation

### SQLite In-Memory / Temp DB
Verwendet Pytest-Fixtures (`db_session`), die vor jedem Testlauf eine saubere Datenbank in einem temporären Verzeichnis aufbauen und nach Abschluss wieder löschen. `data.db` wird bei Tests nicht verändert.

### Temp Image Storage
Das Fixture `temp_image_dir` verwendet `tempfile.TemporaryDirectory()`, um Bild-Upload-Tests vom produktiven `ImageStorage/` Verzeichnis zu isolieren.

### Deterministiche Test-Passwörter
`conftest.py` überschreibt Umgebungsvariablen für Tests mittels Monkeypatch (`ADMIN_PASSWORD="test_admin_pass"`), um von lokalen `.env` Konfigurationen unabhängig zu sein.

## Related pages
- [[database_engine]]
- [[backend_config]]
- [[router_auth]]
