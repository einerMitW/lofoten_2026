# Phase 2: Backend Core (GPX Parser, Database & Sanitizer)

Dieses Dokument beschreibt Phase 2 der Entwicklung der Lofoten 2026 Webapp. In dieser Phase werden die Kern-Logikkomponenten des Backends nach dem TDD-Prinzip entwickelt.

---

## 🎯 Akzeptanzkriterien (Acceptance Criteria)

- **AK-2.1 (GPX Multi-Stage Parsing)**: Das Modul `gpx_parser.py` liest alle 12 GPX-Dateien aus `GpxStorage/` ein, sortiert sie numerisch nach ihren Etappen-Dateinamen (`gt_moskenesoya_0.gpx` bis `gt_austvagoya_10.gpx`) und führt die Trkpts zusammen.
- **AK-2.2 (GeoJSON Transformation)**: Die geparsten Koordinaten werden als valides GeoJSON `FeatureCollection` (Typ `LineString`) mit Koordinaten-Triplets `[longitude, latitude, elevation]` ausgegeben.
- **AK-2.3 (Telemetrie-Berechnung)**: Berechnet präzise Telemetriedaten für die Gesamtroute: Gesamtdistanz (km, via Haversine-Formel), maximale Höhe (m), minimale Höhe (m) und kumulierten Höhengewinn ($\Delta h+$ in Metern).
- **AK-2.4 (SQLite Datenbank)**: Modul `database.py` verwaltet SQLite-Tabellen (`waypoints`) und unterstützt CRUD-Methoden (`create_waypoint`, `get_all_waypoints`, `delete_waypoint`).
- **AK-2.5 (Input & Filename Sanitizer)**: Modul `sanitizer.py` bereinigt Benutzereingaben (`title`, `description`) von HTML/Script-Tags gegen XSS und schützt Dateinamen vor Path-Traversal-Angriffen (z. B. `../`).

---

## 🧪 Test Specifications (Pytest Unit Tests)

### 1. `backend/tests/test_gpx_parser.py`
- `test_parse_single_gpx_file()`: Verifiziert das Einlesen und Extrahieren von Wegpunkten aus `gt_moskenesoya_0.gpx`.
- `test_aggregate_all_12_gpx_files()`: Liest alle 12 Dateien aus `GpxStorage/` ein und prüft, dass 100% der Etappen lückenlos in GeoJSON konvertiert werden.
- `test_haversine_distance()`: Prüft die mathematische Exaktheit der Distanzberechnung zwischen bekannten Geokoordinaten.
- `test_elevation_gain_calculation()`: Testet die korrekte Aufsummierung positiver Höhenunterschiede.
- `test_corrupt_gpx_fallback()`: Testet das Verhalten bei fehlerhaften/beschädigten GPX-Dateien (Graceful Fallback).

### 2. `backend/tests/test_database.py`
- `test_database_table_creation()`: Prüft die automatische Schema-Initialisierung der `waypoints`-Tabelle.
- `test_create_waypoint()`: Fügt einen Wegpunkt ein und verifiziert die vergebene ID sowie Zeitstempel.
- `test_get_all_waypoints()`: Prüft das Abrufen aller gespeicherten Wegpunkte als Liste von Dictionaries.
- `test_delete_waypoint_by_id()`: Löscht einen bestehenden Wegpunkt und prüft, dass dieser nicht mehr in der DB existiert.

### 3. `backend/tests/test_sanitizer.py`
- `test_sanitize_xss_script_tags()`: Wandelt `<script>alert('xss')</script>` in gefilterten Reintext um.
- `test_sanitize_path_traversal()`: Entfernt relative Pfadsegmente wie `../../secret.txt` -> `secret.txt`.

---

## 🚀 Execution Plan (RED -> GREEN -> REFACTOR)

### 1. 🔴 RED Phase
1. Erstellen von `backend/tests/test_gpx_parser.py`, `backend/tests/test_database.py` und `backend/tests/test_sanitizer.py`.
2. Schreiben aller Testfälle mit Behauptungen (Assertions) bezüglich der erwarteten Modul-Schnittstellen.
3. Ausführen der Tests:
   ```bash
   cd backend && pytest tests/test_gpx_parser.py tests/test_database.py tests/test_sanitizer.py
   ```
   *Erwartung:* 100% Fehlschläge (RED), da Module noch nicht existieren.

### 2. 🟢 GREEN Phase
1. Erstellen von `backend/utils/gpx_parser.py`: Implementierung der GPX-Parsing-Funktionen mittels `gpxpy` und Math-Hilfsfunktionen.
2. Erstellen von `backend/database.py`: Implementierung der SQLite-Verbindung und SQL-Statements via `sqlite3`.
3. Erstellen von `backend/utils/sanitizer.py`: Implementierung von Sanitizing-Hilfsfunktionen.
4. Ausführen der Tests:
   ```bash
   cd backend && pytest tests/test_gpx_parser.py tests/test_database.py tests/test_sanitizer.py
   ```
   *Erwartung:* 100% Erfolgreich (GREEN).

### 3. 🔵 REFACTOR Phase
1. Optimierung der Parsing-Performanz für die 12 GPX-Dateien.
2. Typsicherheit mit Python Type Hints (`Dict`, `List`, `Tuple`, `Optional`).
3. Dokumentation aller Funktionen mit Docstrings gemäß [standards.md](file:///C:/Projekte/lofoten_2026/Context/standards.md).
