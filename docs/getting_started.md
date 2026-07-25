# Getting Started

**Summary**: Ausführungs- und Startanleitung der Anwendung im manuellen Modus sowie per Docker Compose.

**Sources**: [[README.md]], [[docker-compose.yml]]

**Last updated**: 2026-07-25

---

Anleitung zum Starten der Anwendung und Ausführen der Testsuiten.

## 1. Manuelles Starten

### Backend starten
```bash
cd backend
python -m uvicorn main:app --port 8085 --reload
```
Das Backend ist unter `http://localhost:8085` erreichbar.

### Frontend starten
```bash
cd frontend
npm run dev
```
Das Frontend ist unter `http://localhost:5173` erreichbar.

---

## 2. Starten über Docker Compose

Erstellt und startet beide Container im Hintergrund:

```bash
docker-compose up --build -d
```

Die Anwendung ist über das Loopback-Binding unter **`http://127.0.0.1:5567`** erreichbar.

### Docker Container stoppen
```bash
docker-compose down
```

---

## 3. Tests ausführen

### Backend (Pytest)
```bash
cd backend
python -m pytest
```

### Frontend (Vitest)
```bash
cd frontend
npm run test
```

## Related pages
- [[setup_guide]]
- [[deployment_network]]
- [[api_endpoints]]
