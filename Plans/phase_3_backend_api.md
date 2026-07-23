# Phase 3: Backend REST API & Authentifizierung

Dieses Dokument beschreibt Phase 3 der Entwicklung der Lofoten 2026 Webapp. In dieser Phase wird die FastAPI-Rest-Schnittstelle aufgebaut und gegen unbefugte Zugriffe abgesichert.

---

## 🎯 Akzeptanzkriterien (Acceptance Criteria)

- **AK-3.1 (Routen-Endpunkt `GET /api/route`)**: Liefert das zusammengefasste GeoJSON aller 12 GPX-Etappen inkl. Telemetriedaten (Distanz, Höhenprofil, Min/Max-Höhe) mit HTTP 200 zurück.
- **AK-3.2 (Wegpunkt-Abruf `GET /api/waypoints`)**: Liefert alle gespeicherten Wegpunkte aus der Datenbank als JSON-Array mit HTTP 200 zurück.
- **AK-3.3 (Admin-Login `POST /api/auth/login`)**: Verifiziert das eingegebene Passwort gegen `ADMIN_PASSWORD` aus der `.env`. Bei Erfolg wird HTTP 200 inkl. Session-Token zurückgegeben. Bei falschem Passwort HTTP 401 Unauthorized.
- **AK-3.4 (Geschützte Endpunkte & Auth-Shield)**: `POST /api/waypoints`, `DELETE /api/waypoints/{id}` und `POST /api/images` verlangen ein gültiges Auth-Header/Token. Ohne Token antwortet das Backend sofort mit HTTP 401 Unauthorized.
- **AK-3.5 (Bild-Upload & Validierung `POST /api/images`)**: Nimmt Multipart-Uploads entgegen, prüft die Dateiendung (`.jpg`, `.jpeg`, `.png`, `.webp`), speichert sie in `ImageStorage/` und gibt die Bild-URL zurück. Ungültige Dateitypen werden mit HTTP 400 Bad Request abgelehnt.
- **AK-3.6 (Statische Bildausgabe `GET /api/images/{filename}`)**: Liefert hochgeladene Bilder aus `ImageStorage/` mit dem passenden `Content-Type` Header aus.

---

## 🧪 Test Specifications (Pytest Integration Tests)

### 1. `backend/tests/test_api_auth.py`
- `test_login_success()`: Testet `POST /api/auth/login` mit korrektem Passwort -> HTTP 200 + Token.
- `test_login_wrong_password()`: Testet `POST /api/auth/login` mit falschem Passwort -> HTTP 401.

### 2. `backend/tests/test_api_route.py`
- `test_get_route_structure()`: Testet `GET /api/route` und verifiziert GeoJSON-Schema, Koordinaten-Anzahl und Telemetriefelder.

### 3. `backend/tests/test_api_waypoints.py`
- `test_get_waypoints_empty_initial()`: `GET /api/waypoints` liefert leeres Array `[]`.
- `test_create_waypoint_unauthorized()`: `POST /api/waypoints` ohne Auth-Header liefert HTTP 401.
- `test_create_waypoint_authorized()`: `POST /api/waypoints` mit Auth-Token legt Eintrag an und liefert HTTP 201.
- `test_delete_waypoint_authorized()`: `DELETE /api/waypoints/{id}` löscht Eintrag aus DB und Bilddatei von Festplatte.

### 4. `backend/tests/test_api_images.py`
- `test_upload_image_invalid_extension()`: Upload einer `.exe` oder `.sh` Datei schlägt mit HTTP 400 fehl.
- `test_upload_image_success()`: Upload einer `.jpg` Datei speichert Datei in `ImageStorage/` ab.
- `test_serve_image_static()`: `GET /api/images/{filename}` liefert Binärdaten mit `image/jpeg` Content-Type.

---

## 🚀 Execution Plan (RED -> GREEN -> REFACTOR)

### 1. 🔴 RED Phase
1. Schreiben von `backend/tests/test_api_auth.py`, `backend/tests/test_api_route.py`, `backend/tests/test_api_waypoints.py` und `backend/tests/test_api_images.py` unter Verwendung des FastAPI `TestClient` (aus `httpx`).
2. Ausführen der API-Integrationstests:
   ```bash
   cd backend && pytest tests/test_api_*.py
   ```
   *Erwartung:* 100% Fehlschläge (RED).

### 2. 🟢 GREEN Phase
1. Erstellen von `backend/config.py` zum Einlesen der `.env`-Variablen (`ADMIN_PASSWORD`).
2. Erstellen der Router-Module in `backend/routers/`:
   - `auth.py`
   - `gpx.py`
   - `waypoints.py`
   - `images.py`
3. Erstellen von `backend/main.py` mit FastAPI-App, CORS-Middleware und Router-Einbindung.
4. Ausführen der Tests:
   ```bash
   cd backend && pytest tests/test_api_*.py
   ```
   *Erwartung:* 100% Erfolgreich (GREEN).

### 3. 🔵 REFACTOR Phase
1. Einheitliche Fehlerbehandlung mit custom `HTTPException` Handlern.
2. Saubere Trennung von Routern, Services und Datenbankabfragen.
