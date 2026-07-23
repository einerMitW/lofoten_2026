# Phase 4: Frontend Core (Design System, Karte & Höhenprofil)

Dieses Dokument beschreibt Phase 4 der Entwicklung der Lofoten 2026 Webapp. In dieser Phase werden das Frontend-Layout, das Design-System gemäß [DESIGN.md](file:///C:/Projekte/lofoten_2026/Context/DESIGN.md), die Leaflet-Karten-Komponente und das interaktive Höhenprofil entwickelt.

---

## 🎯 Akzeptanzkriterien (Acceptance Criteria)

- **AK-4.1 (Arctic Tech Design System)**: `style.css` setzt alle Design-Tokens strikt um: Farbschema (`--bg`, `--surface`, `--accent` `#ff4a5a`), Glasmorphismus (`backdrop-filter: blur(16px)`), Typografie (`Inter` für Fließtext, `JetBrains Mono` mit `tabular-nums` für Daten/Telemetrie).
- **AK-4.2 (Leaflet Dark Sage CSS-Filter)**: Der Karten-Layer nutzt den CSS-Matrix-Filter (`filter: sepia(1) hue-rotate(130deg) saturate(3) brightness(1.7) contrast(1.3)`), um Basiskarten ins arktische Waldtürkis einzufärben.
- **AK-4.3 (Routen-Darstellung)**: `MapView.vue` lädt das GeoJSON der 12 Etappen via `api.js` und zeichnet die Wanderroute als leuchtend rote Polyline (`--accent`).
- **AK-4.4 (Höhenprofil & Laser Scrubber)**: `ElevationProfile.vue` rendert ein SVG-Höhenprofil-Diagramm. Beim Bewegen der Maus über das Diagramm gleitet ein Laser-Pointer-Scrubber mit und hebt die entsprechende Geokoordinate auf der Karte hervor.
- **AK-4.5 (Telemetrie HUD)**: Das HUD-Panel zeigt Gesamtdistanz, Höhenmeter und "LIVE"-Badge an.

---

## 🧪 Test Specifications (Vitest Unit Tests)

### 1. `frontend/src/services/__tests__/api.spec.js`
- `test_fetch_route_api()`: Mocks `fetch('/api/route')` und prüft die GeoJSON-Rückgabe.
- `test_fetch_waypoints_api()`: Mocks `fetch('/api/waypoints')` und prüft die Datenstruktur.

### 2. `frontend/src/components/__tests__/ElevationProfile.spec.js`
- `test_renders_svg_path_with_data()`: Verifiziert, dass ein `<path>`-Element gerendert wird, sobald `routeData`-Props übergeben werden.
- `test_emits_scrub_event_on_mousemove()`: Prüft, ob bei Mausbewegung auf dem Chart ein `scrub`-Event mit der aktuellen Distanz und Koordinate ausgelöst wird.
- `test_calculates_telemetry_totals()`: Prüft die mathematische Aufbereitung der Min/Max-Höhen und Distanzen im Chart.

### 3. `frontend/src/components/__tests__/MapView.spec.js`
- `test_initializes_leaflet_map()`: Verifiziert die Erzeugung des Leaflet Container DOM-Elements.
- `test_updates_scrubber_marker_position()`: Prüft, ob der Marker-Punkt auf der Karte verschoben wird, wenn ein `scrub`-Event empfangen wird.

---

## 🚀 Execution Plan (RED -> GREEN -> REFACTOR)

### 1. 🔴 RED Phase
1. Erstellen aller Testdateien in `frontend/src/**/__tests__/`.
2. Ausführen von Vitest:
   ```bash
   cd frontend && npx vitest run
   ```
   *Erwartung:* 100% Fehlschläge (RED).

### 2. 🟢 GREEN Phase
1. Erstellen von `frontend/src/style.css` mit allen CSS-Variablen und Utilities aus `DESIGN.md`.
2. Erstellen von `frontend/src/services/api.js` für Backend-Aufrufe (`fetch`).
3. Erstellen von `frontend/src/components/MapView.vue` (Leaflet Map Integration).
4. Erstellen von `frontend/src/components/ElevationProfile.vue` (SVG Scrubber Chart).
5. Erstellen von `frontend/src/views/HomeView.vue` und `frontend/src/App.vue`.
6. Ausführen der Tests:
   ```bash
   cd frontend && npx vitest run
   ```
   *Erwartung:* 100% Erfolgreich (GREEN).

### 3. 🔵 REFACTOR Phase
1. Absichern von `prefers-reduced-motion` in CSS-Animationen.
2. Tastatur-Navigierbarkeit (`tabindex="0"`, `:focus-visible`) für das Höhenprofil.
