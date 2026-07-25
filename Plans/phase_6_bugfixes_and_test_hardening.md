# Phase 6: Bugfixes & Test-Hardening (E2E Findings)

Dieses Dokument beschreibt Phase 6 der Entwicklung der Lofoten 2026 Webapp. In dieser Phase werden die im manuellen E2E-Test gefundenen Punkte aus `todo.md` nach dem TDD-Prinzip behoben und die Testinfrastruktur gehärtet.

---

## 🎯 Akzeptanzkriterien (Acceptance Criteria)

- **AK-6.1 (GPX Laufrichtung-Autoausrichtung)**: `gpx_parser.py` erkennt beim Zusammenfügen aufeinanderfolgender GPX-Etappen (`gt_moskenesoya_0.gpx` bis `gt_austvagoya_10.gpx`), ob eine Etappe in umgekehrter Richtung aufgezeichnet wurde (`dist_end < dist_start`), und invertiert die Punkteliste (`points.reverse()`), sodass der Routen-Cursor durchgehend monotonic von Moskenesøya nach Austvågøya verläuft.
- **AK-6.2 (Scrubber Marker Persistenz)**: `MapView.vue` verwendet eine dedizierte Leaflet-Layer-Gruppe (`scrubberLayer`) für den Laser-Scrubber-Marker. Der Marker bleibt bei Karteninteraktionen (Zoom, Pan, Klick) erhalten und wird nur bei explizitem `mouseleave` aus dem Chart gelöscht.
- **AK-6.3 (.env Vorlage & Konfiguration)**: `backend/.env.example` stellt die Umgebungsvariablen-Vorlage bereit. `config.py` liest `.env` via `python-dotenv` ein. Fehlt `ADMIN_PASSWORD`, wird ein klarer Konfigurationsfehler ausgegeben.
- **AK-6.4 (Test-Datenbank & Bild-Speicher Isolation)**: Pytest-Fixtures in `conftest.py` nutzen eine temporäre SQLite-Testdatenbank sowie ein temporäres Bild-Verzeichnis (`tempfile.TemporaryDirectory()`). Testläufe hinterlassen keine Dateien in `data.db` oder `ImageStorage/`.
- **AK-6.5 (Determinische Test-Passwörter)**: `conftest.py` überschreibt `ADMIN_PASSWORD` per Pytest-Monkeypatch auf den festen Wert `"test_admin_pass"`. Tests hängen nicht von lokalen `.env`-Passwörtern ab.

---

## 🧪 Test Specifications (Pytest & Vitest)

### Backend Tests (`backend/tests/`)
- `test_gpx_parser.py`:
  - `test_gpx_stage_direction_auto_alignment()`: Verifiziert, dass Etappen mit umgekehrter Koordinatenfolge automatisch gedreht werden.
- `conftest.py`:
  - Fixtures zur vollständigen Isolation von DB und Bild-Ordner während der Tests.

### Frontend Tests (`frontend/src/components/__tests__/`)
- `MapView.spec.js`:
  - `test_scrubber_layer_persistence()`: Verifiziert, dass der Scrubber-Marker in einem separaten Layer-Group verwaltet wird.

---

## 🚀 Execution Plan (RED -> GREEN -> REFACTOR)

### 1. 🔴 RED Phase
1. Aktualisieren von `backend/tests/test_gpx_parser.py` und `backend/tests/conftest.py`.
2. Schreiben des fehlschlagenden Testfalls für GPX-Laufrichtungsausrichtung.
3. Ausführen der Tests: `cd backend && python -m pytest`

### 2. 🟢 GREEN Phase
1. `backend/utils/gpx_parser.py`: Implementierung der Richtungsprüfung (`dist_end < dist_start`).
2. `backend/config.py`: Konfigurationsprüfung & `.env.example` Erstellung.
3. `backend/tests/conftest.py`: Isolation von Test-DB & Temp-Image-Folder + Monkeypatch für Test-Passwort.
4. `frontend/src/components/MapView.vue`: Dediziertes `scrubberLayer`.
5. Ausführen aller Tests: `pytest` & `vitest`.

### 3. 🔵 REFACTOR Phase
1. Überprüfen, dass `data.db` und `ImageStorage/` nach den Tests 100% sauber sind.
