# Lofoten 2026 – Web Application

Eine moderne Webanwendung zur Aufbereitung und interaktiven Erkundung der Lofoten-Überquerung 2026.

## Features
- **Interaktive Karte**: Leaflet-Karte im **Arctic Tech / Dark Sage** Stil (`DESIGN.md`) mit Anzeige aller 12 Etappen-GPX-Tracks aus `GpxStorage/`.
- **Höhenprofil & Laser-Scrubber**: Interaktives SVG-Höhenprofil-Diagramm synchronisiert Mauspositionen live mit Koordinaten-Punkten auf der Karte.
- **Telemetrie HUD**: Berechnung von Gesamtdistanz, kumuliertem Höhengewinn sowie Min/Max-Höhen.
- **Bild-Popups**: Glasmorphes Foto-Story Modal für Fotopunkte entlang der Wanderroute.
- **Admin-Bereich (`/wal`)**: Passwortgeschützter Bereich zum Platzieren neuer Wegpunkte per Klick auf die Karte mit Foto-Upload.

---

## Lokales Starten

### 1. Backend (FastAPI + Python)
```bash
cd backend
python -m venv venv
# Windows PowerShell:
.\venv\Scripts\activate
pip install -r requirements.txt

# Start Backend Server (Port 8085)
python -m uvicorn main:app --port 8085 --reload
```

### 2. Frontend (Vue 3 + Vite)
```bash
cd frontend
npm install

# Start Frontend Dev Server (Port 5173)
npm run dev
```

---

## Tests Ausführen (TDD)

### Backend Tests (Pytest)
```bash
cd backend
python -m pytest
```

### Frontend Tests (Vitest)
```bash
cd frontend
npm run test
```
