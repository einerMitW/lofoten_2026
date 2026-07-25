# GPX Parser Core

**Summary**: Kernmodul zur Extrahierung von Geokoordinaten und Höhendaten aus GPX-Dateien mittels gpxpy.

**Sources**: [[backend/utils/gpx_parser.py]]

**Last updated**: 2026-07-25

---

Die Komponente `gpx_parser_core` verwendet die Python-Bibliothek `gpxpy` zur Analyse strukturierter XML-GPX-Dateien.

## Verarbeitungslogik

### XML Parsing
Das Modul durchläuft GPX-Tracks (`gpx.tracks`), Segmente (`segment.points`) und liest für jeden Wegpunkt Breitengrad (`lat`), Längengrad (`lon`) sowie Höhenangaben (`elevation`) aus.

### Fehlerbehandlung & Fallbacks
Falls Höhenwerte in einzelnen Punkten fehlen, führt das Modul lineare Interpolationen durch oder setzt den Wert auf 0, um Konsistenz im Profil zu wahren.

## Related pages
- [[gpx_auto_alignment]]
- [[gpx_metrics]]
- [[router_gpx]]
