# Setup Guide

**Summary**: Schritt-für-Schritt Anleitung zur Einrichtung der Entwicklungsumgebung (manuell & Docker).

**Sources**: [[backend/requirements.txt]], [[frontend/package.json]], [[docker-compose.yml]]

**Last updated**: 2026-07-25

---

Dieser Leitfaden beschreibt das Setup der Lofoten 2026 Anwendung sowohl für die lokale Entwicklung als auch für das Docker-Deployment.

## Systemvoraussetzungen

- **Python**: Version 3.11 oder höher
- **Node.js**: Version 20.x LTS oder höher
- **Docker**: Docker Engine 24+ und Docker Compose v2+

---

## 1. Manuelles Setup (Entwicklung)

### Backend Einrichtung
1. Navigieren Sie in den Ordner `backend`:
   ```bash
   cd backend
   ```
2. Virtuelle Umgebung erstellen und aktivieren:
   ```bash
   python -m venv venv
   # Windows PowerShell:
   .\venv\Scripts\activate
   ```
3. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```
4. Umgebungsvariablen anlegen:
   Kopieren Sie `backend/.env.example` nach `backend/.env` und legen Sie `ADMIN_PASSWORD` fest.

### Frontend Einrichtung
1. Navigieren Sie in den Ordner `frontend`:
   ```bash
   cd frontend
   ```
2. Node-Pakete installieren:
   ```bash
   npm ci
   ```

---

## 2. Docker Setup (Containerisierung)

1. Kopieren Sie die Vorlage `.env.example` im Stammverzeichnis nach `.env`:
   ```bash
   cp .env.example .env
   ```
2. Stellen Sie sicher, dass Docker und Docker Compose installiert sind.

## Related pages
- [[getting_started]]
- [[deployment_network]]
- [[project_overview]]
