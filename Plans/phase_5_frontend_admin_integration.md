# Phase 5: Frontend Admin, Popups & End-to-End Integration

Dieses Dokument beschreibt Phase 5 der Entwicklung der Lofoten 2026 Webapp. In dieser Phase werden die Bild-Popup-Modals für Besucher sowie der geschützte Admin-Bereich unter `/wal` für den Foto-Upload per Klick auf die Karte implementiert.

---

## 🎯 Akzeptanzkriterien (Acceptance Criteria)

- **AK-5.1 (Bilder-Popup Modal `ImagePopup.vue`)**: Klick auf einen Wegpunkt-Pin auf der Karte öffnet ein flüssig animiertes Glas-Modal mit geblurrtem Hintergrund (`backdrop-filter: blur(16px)`), das das Foto, den Titel und die Kurzbeschreibung anzeigt.
- **AK-5.2 (Admin-Route `/wal` & Login Modal `AdminLogin.vue`)**: Der Aufruf der Route `/wal` zeigt eine Login-Maske. Die Eingabe des korrekten Passworts speichert das Auth-Token im Speicher und schaltet die Admin-Karte frei.
- **AK-5.3 (Klick-auf-Karte für Wegpunkte `AdminPanel.vue`)**: Im Admin-Modus bewirkt ein Klick auf eine beliebige Stelle der Karte das Öffnen des Upload-Dialogs (`ImageUpload.vue`) mit vorausgefüllten Lat/Lng-Koordinaten.
- **AK-5.4 (Wegpunkt & Foto Upload `ImageUpload.vue`)**: Das Formular erlaubt das Auswählen einer Bilddatei, die Eingabe von Titel & Beschreibung und sendet die Daten an `POST /api/images` und `POST /api/waypoints`. Nach erfolgreichem Upload erscheint der neue Marker sofort auf der Karte und bleibt nach einem Page-Reload persistent.
- **AK-5.5 (End-to-End Integration)**: Das Gesamtsystem (FastAPI Backend + Vue Frontend) funktioniert fehlerfrei zusammen.

---

## 🧪 Test Specifications (Vitest Integration Tests & E2E Verification)

### 1. `frontend/src/components/__tests__/ImagePopup.spec.js`
- `test_popup_opens_with_waypoint_data()`: Verifiziert, dass Bild-URL, Titel und Beschreibung im Modal gerendert werden, wenn ein Wegpunkt ausgewählt ist.
- `test_popup_closes_on_overlay_click()`: Prüft das Schließen des Modals bei Klick auf den Hintergrund oder Close-Button.

### 2. `frontend/src/views/__tests__/AdminView.spec.js`
- `test_admin_login_flow()`: Prüft die Interaktion der Login-Maske (Eingabe -> API Call -> Token Speicherung -> Ansichtsübergang).
- `test_admin_map_click_captures_coordinates()`: Simuliert einen Klick auf die Karte im Admin-Modus und verifiziert das Öffnen des Upload-Formulars mit exakten Lat/Lng-Werten.
- `test_upload_form_submission()`: Simuliert die Formularabgabe und prüft, dass der API-Client aufgerufen und ein neuer Marker gerendert wird.

---

## 🚀 Execution Plan (RED -> GREEN -> REFACTOR)

### 1. 🔴 RED Phase
1. Erstellen von `frontend/src/components/__tests__/ImagePopup.spec.js` und `frontend/src/views/__tests__/AdminView.spec.js`.
2. Ausführen von Vitest:
   ```bash
   cd frontend && npx vitest run
   ```
   *Erwartung:* 100% Fehlschläge (RED).

### 2. 🟢 GREEN Phase
1. Erstellen von `frontend/src/components/ImagePopup.vue` (Foto-Story Modal).
2. Erstellen von `frontend/src/components/AdminLogin.vue` (Passwort-Login Modal).
3. Erstellen von `frontend/src/components/ImageUpload.vue` (Foto & Wegpunkt Upload Formular).
4. Erstellen von `frontend/src/views/AdminView.vue` und Routing in `frontend/src/router/index.js` für `/wal`.
5. Ausführen aller Frontend-Tests:
   ```bash
   cd frontend && npx vitest run
   ```
   *Erwartung:* 100% Erfolgreich (GREEN).

### 3. 🔵 REFACTOR & E2E Systemverifikation Phase
1. Gesamten Backend Testsuite ausführen:
   ```bash
   cd backend && pytest
   ```
2. Gesamten Frontend Testsuite ausführen:
   ```bash
   cd frontend && npx vitest run
   ```
3. Anwendung lokal starten und manuelles End-to-End Szenario durchspielen:
   - Backend starten: `cd backend && uvicorn main:app --reload`
   - Frontend starten: `cd frontend && npm run dev`
   - Öffnen von `http://localhost:5173` -> Route aus den 12 GPX-Dateien prüfen, Höhenprofil bedienen.
   - Öffnen von `http://localhost:5173/wal` -> Einloggen, Klick auf Karte, Bild hochladen -> Dauerhafte Speicherung auf der Karte überprüfen.
