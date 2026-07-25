# C4 Architecture Model

**Summary**: Gesamtsystem-Architektur nach dem C4-Modell (Context, Container, Components, Code).

**Sources**: [[c4_model/overview.md]]

**Last updated**: 2026-07-25

---

Die Komponente `c4_architecture_model` beschreibt die strukturelle Architektur der Lofoten 2026 Anwendung auf verschiedenen Abstraktionsebenen.

## Modell-Ebenen

### System Context
Benutzer (Wanderer, Administratoren) interagieren mit der Single-Page Web-Anwendung zur Erkundung der Lofoten-Route.

### Containers
- **Frontend Container**: Vue 3 SPA für Karten- und Höhenprofilvisualisierung.
- **Backend Container**: FastAPI App für REST-APIs, GPX-Parsing und Authentifizierung.
- **Database Container**: SQLite Datei-Datenbank `data.db`.
- **Storage Container**: Dateisystem-Ordner `ImageStorage/` für hochgeladene Medien.

### Components & Code
Detaillierte Beschreibungen der internen Bausteine finden sich in den jeweiligen Sub-Seiten des Wikis.

## Related pages
- [[backend_main]]
- [[frontend_main]]
- [[database_engine]]
