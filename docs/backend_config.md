# Backend Configuration

**Summary**: zentrales Konfigurationsmodul zum Laden von Umgebungsvariablen, Datenbankpfaden und Authentifizierungs-Geheimnissen.

**Sources**: [[backend/config.py]], [[backend/.env]]

**Last updated**: 2026-07-25

---

Das Modul `backend_config` stellt sämtliche Umgebungsvariablen und Pfadkonfigurationen zentral für das Backend bereit.

## Konfigurationsparameter

### Umgebungsvariablen (`.env`)
Mittels `python-dotenv` werden Variablen aus der lokalen `.env`-Datei geladen:
- `SECRET_KEY`: Geheimer Schlüssel zur Signierung von JWT-Tokens.
- `ADMIN_PASSWORD`: Passwort für den Administrator-Zugang.
- `DATABASE_URL`: Verbindungs-String für die SQLite-Datenbank.
- `IMAGE_DIR`: Dateisystem-Pfad zur Speicherung hochgeladener Fotos.

### Pfad-Abstraktion
Das Modul definiert absolute Pfade für das Projektverzeichnis, um plattformunabhängige Zugriffe auf `data.db` und den Bilderspeicher `ImageStorage/` zu gewährleisten.

### Fehlerbehandlung bei Konfiguration
Sollten kritische Variablen wie `ADMIN_PASSWORD` nicht gesetzt sein, bricht das Modul mit einem expliziten Konfigurationsfehler ab, um unsichere Standardeinstellungen zu verhindern.

## Related pages
- [[backend_main]]
- [[database_engine]]
- [[router_auth]]
