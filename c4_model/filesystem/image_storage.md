# ImageStorage

| Eigenschaft | Wert |
|:---|:---|
| **Name** | ImageStorage |
| **Container** | Dateisystem |
| **Sprache** | – (Dateisystem-Konvention) |

## Aufgabe
Definiert die Konvention für die Ablage von hochgeladenen Bilddateien. Bilder werden vom [ImageRouter](../backend/image_router.md) beim Upload hierhin geschrieben und vom Backend als statische Dateien ausgeliefert.

### Verzeichnisstruktur
```
backend/
└── data/
    └── uploads/
        └── images/
            ├── a3b2c1d4-5678-9012-ef34-567890abcdef.jpg
            ├── f1e2d3c4-b5a6-7890-1234-567890abcdef.png
            └── ...
```

### Regeln
- Dateinamen werden vom Backend als **UUID v4** generiert (z.B. `uuid4.jpg`), um Kollisionen und bösartige Dateinamen zu verhindern.
- Der relative Pfad (z.B. `uploads/images/uuid4.jpg`) wird als `image_path` in der [Schema](../database/schema.md)-Tabelle `waypoints` gespeichert.
- Akzeptierte MIME-Types: `image/jpeg`, `image/png`, `image/webp`.
- Das Backend hat **Lese- und Schreibrechte** auf dieses Verzeichnis.
- Beim Löschen eines Wegpunktes muss die zugehörige Bilddatei ebenfalls physisch gelöscht werden.

## Begründung
Die Ablage von Bildern im Dateisystem (statt als BLOB in der Datenbank) ist Best Practice, weil:
1. Webserver liefern statische Dateien direkt und performant aus.
2. Die SQLite-Datei bleibt klein (Kilobytes statt Megabytes).
3. Backups der Bilder sind einfach (Ordner kopieren).

**User Story Bezug:** UC-5 (Bilder hochladen), UC-6 (persistente Speicherung)

## Abhängigkeiten
- **Intern:**
  - Wird beschrieben von → [ImageRouter](../backend/image_router.md)
  - Wird referenziert in → [Schema](../database/schema.md) (`image_path`-Spalte)
  - Bilder werden angezeigt in → [ImagePopup](../frontend/image_popup.md) (Frontend)
