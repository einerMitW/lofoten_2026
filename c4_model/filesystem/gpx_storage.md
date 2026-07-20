# GpxStorage

| Eigenschaft | Wert |
|:---|:---|
| **Name** | GpxStorage |
| **Container** | Dateisystem |
| **Sprache** | – (Dateisystem-Konvention) |

## Aufgabe
Definiert die Konvention für die Ablage von GPX-Dateien auf dem Server. GPX-Dateien werden **manuell** vom Entwickler/Admin bereitgestellt und vom Backend nur **gelesen** (Read-Only).

### Verzeichnisstruktur
```
backend/
└── data/
    └── gpx/
        ├── lofoten_tag1.gpx
        ├── lofoten_tag2.gpx
        └── ...
```

### Regeln
- GPX-Dateien werden **nicht** über die Web-API hochgeladen, sondern direkt im Dateisystem abgelegt.
- Das Backend hat **nur Leserechte** auf dieses Verzeichnis (Least Privilege, vgl. developer_dialog.md Abschnitt 7).
- Dateinamen sollten sprechend sein (z.B. nach Tagesetappen).

## Begründung
Die GPX-Daten ändern sich nach dem Urlaub nicht mehr. Ein Upload-Mechanismus wäre Overengineering. Es reicht, die Dateien einmalig im Dateisystem bereitzustellen.

**User Story Bezug:** UC-1 (Route sehen)

## Abhängigkeiten
- **Intern:**
  - Wird gelesen von → [GpxParser](../backend/gpx_parser.md)
