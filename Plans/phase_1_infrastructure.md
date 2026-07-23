# Phase 1: TDD-Infrastruktur & Projekt-Setup

Dieses Dokument beschreibt Phase 1 der Entwicklung der Lofoten 2026 Webapp. Ziel dieser Phase ist das Erstellen der Ordnerstruktur (`/backend` und `/frontend`) sowie das Aufsetzen der TDD-Testinfrastruktur (Pytest für Python Backend, Vitest für Vue Frontend), sodass Vorab-Tests geschrieben und im **RED-Zustand** ausgeführt werden können.

---

## 🎯 Akzeptanzkriterien (Acceptance Criteria)

- **AK-1.1**: Die Ordnerstruktur `/backend` und `/frontend` existiert im Monorepo.
- **AK-1.2**: Backend-Abhängigkeiten (`fastapi`, `uvicorn`, `gpxpy`, `pytest`, `httpx`, `python-dotenv`) sind in `backend/requirements.txt` definiert.
- **AK-1.3**: Pytest ist im Backend einsatzbereit und findet Testdateien im Ordner `backend/tests/`.
- **AK-1.4**: Frontend-Projekt (Vue 3 + Vite + Vitest) ist in `/frontend` initialisiert mit `package.json` und `vite.config.js`.
- **AK-1.5**: Vitest ist im Frontend einsatzbereit und führt Testdateien in `frontend/src/**/__tests__/` aus.
- **AK-1.6**: Erster Testlauf von `pytest` im Backend und `vitest` im Frontend liefert geplante Fehlschläge (**RED State**) für alle noch nicht implementierten Module.

---

## 🧪 Test Specifications

### Backend Tests (`backend/tests/`)
- `backend/tests/conftest.py`: Fixtures für In-Memory SQLite Testdatenbank, temporäre Test-Bildordner und Mock-GPX-Dateien.
- `backend/tests/test_health.py`:
  - `test_pytest_environment_works()`: Prüft, ob Pytest Test-Fixtures korrekt lädt.

### Frontend Tests (`frontend/src/__tests__/`)
- `frontend/src/__tests__/setup.spec.js`:
  - `test_vitest_environment_works()`: Prüft, ob Vitest in der jsdom-Umgebung läuft.

---

## 🚀 Execution Plan (RED -> GREEN -> REFACTOR)

### 1. 🔴 RED Phase
1. Anlegen der Verzeichnisse `/backend`, `/backend/tests`, `/frontend`, `/frontend/src`.
2. Anlegen von `backend/requirements.txt` mit allen Test- und Runtime-Abhängigkeiten.
3. Anlegen von `frontend/package.json` und `frontend/vite.config.js` inkl. Vitest & jsdom Konfiguration.
4. Schreiben von `backend/tests/test_health.py` und `frontend/src/__tests__/setup.spec.js`.
5. Ausführen der Test-Runner:
   ```bash
   cd backend && pytest
   cd frontend && npx vitest run
   ```

### 2. 🟢 GREEN Phase
1. Installieren der Python-Abhängigkeiten im Venv.
2. Installieren der Node-Abhängigkeiten via `npm install`.
3. Ausführen der Tests zur Bestätigung der grünen Infrastruktur.

### 3. 🔵 REFACTOR Phase
1. Konfigurieren der Pytest-Optionen in `backend/pytest.ini` oder `pyproject.toml`.
2. Konfigurieren der Vitest-Optionen und Alias-Pfade (`@/` -> `src/`) in `frontend/vite.config.js`.
