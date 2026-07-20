# C4 Modell – Lofoten 2026 Web App

Dieses Dokument beschreibt die Architektur der Lofoten 2026 Webapp auf den C4-Ebenen **Context**, **Container** und **Component**.
Die Entscheidungen basieren auf dem [developer_dialog.md](../Context/developer_dialog.md).

---

## Level 1 – System Context

Wer interagiert mit dem System und welche externen Abhängigkeiten gibt es?

```mermaid
graph LR
    Anwender["👤 Anwender<br/>(Anonymer Besucher)"]
    Admin["🔑 Admin<br/>(Passwort-authentifiziert)"]
    System["🗺️ Lofoten 2026<br/>Web App"]
    Mapbox["🌍 Mapbox API<br/>(Externer Dienst)"]

    Anwender -- "Betrachtet Route,<br/>öffnet Bilder-Popups" --> System
    Admin -- "Lädt Bilder hoch,<br/>verwaltet Wegpunkte" --> System
    System -- "Lädt Karten-Tiles<br/>& Vektor-Daten" --> Mapbox
```

| Akteur / System | Beschreibung |
|:---|:---|
| **Anwender** | Anonymer Besucher, der die Route auf der Karte betrachtet und Bilder-Popups öffnet. |
| **Admin** | Authentifiziert sich über `/wal` mit einem Passwort und kann Wegpunkte mit Bildern auf der Karte platzieren. |
| **Mapbox API** | Externer Kartendienst, der Vektor-Tiles und Styling-Ressourcen bereitstellt. |

---

## Level 2 – Container

Aus welchen deploybare Einheiten besteht das System?

```mermaid
graph TB
    subgraph "Lofoten 2026 System"
        FE["🖥️ Frontend<br/>(Vue.js SPA)"]
        BE["⚙️ Backend<br/>(FastAPI / Python)"]
        DB[("💾 SQLite<br/>Datenbank")]
        FS["📁 Dateisystem<br/>(GPX + Bilder)"]
    end

    Mapbox["🌍 Mapbox API"]

    FE -- "REST API Calls<br/>(HTTP/JSON)" --> BE
    BE -- "SQL Queries" --> DB
    BE -- "Lesen/Schreiben<br/>von Dateien" --> FS
    FE -- "Karten-Tiles laden" --> Mapbox
```

| Container | Technologie | Beschreibung | Komponenten |
|:---|:---|:---|:---|
| **Frontend** | Vue.js + Vanilla CSS | Single Page Application, rendert Karte, Route, Popups und Admin-UI. | [→ Komponenten](frontend/) |
| **Backend** | FastAPI (Python) | REST API für GPX-Parsing, Bild-Upload, Wegpunkt-CRUD und Authentifizierung. | [→ Komponenten](backend/) |
| **Datenbank** | SQLite | Speichert Wegpunkt-Metadaten (Koordinaten, Beschreibung, Bildpfad). | [→ Schema](database/) |
| **Dateisystem** | OS Filesystem | Persistente Ablage für GPX-Dateien und hochgeladene Bilddateien. | [→ Struktur](filesystem/) |

---

## Level 3 – Component

### Frontend-Komponenten (Vue.js)

```mermaid
graph TB
    subgraph "Frontend Container – Vue.js SPA"
        MapView["🗺️ MapView<br/><i>Mapbox Karte</i>"]
        RouteLayer["📍 RouteLayer<br/><i>GeoJSON Route</i>"]
        ElevationProfile["📈 ElevationProfile<br/><i>Höhenprofil</i>"]
        WaypointMarker["📌 WaypointMarker<br/><i>Bilder-Marker</i>"]
        ImagePopup["🖼️ ImagePopup<br/><i>Bild-Overlay</i>"]
        AdminLogin["🔐 AdminLogin<br/><i>/wal Login</i>"]
        AdminPanel["⚙️ AdminPanel<br/><i>Admin-Karte</i>"]
        ImageUpload["📤 ImageUpload<br/><i>Upload-Dialog</i>"]
        ApiClient["🔗 ApiClient<br/><i>HTTP-Client</i>"]
    end

    MapView -- "stellt Map-Instanz bereit" --> RouteLayer
    MapView -- "stellt Map-Instanz bereit" --> WaypointMarker
    MapView -- "stellt Map-Instanz bereit" --> AdminPanel
    RouteLayer -- "liefert Höhendaten" --> ElevationProfile
    WaypointMarker -- "öffnet bei Klick" --> ImagePopup
    AdminLogin -- "leitet weiter nach Login" --> AdminPanel
    AdminPanel -- "öffnet bei Klick auf Karte" --> ImageUpload
    ImageUpload -. "teilt UI-Basis mit" .-> ImagePopup

    RouteLayer -- "GET /api/route" --> ApiClient
    WaypointMarker -- "GET /api/waypoints" --> ApiClient
    AdminLogin -- "POST /api/auth/login" --> ApiClient
    ImageUpload -- "POST /api/waypoints" --> ApiClient
```

| Komponente | Aufgabe | Datei |
|:---|:---|:---|
| **MapView** | Initialisiert und rendert die Mapbox GL JS Karte. | [map_view.md](frontend/map_view.md) |
| **RouteLayer** | Zeichnet die GPX-Route als GeoJSON-Layer auf die Karte. | [route_layer.md](frontend/route_layer.md) |
| **ElevationProfile** | Rendert das Höhenprofil der Route. *(Post-MVP)* | [elevation_profile.md](frontend/elevation_profile.md) |
| **WaypointMarker** | Platziert Bilder-Wegpunkte als Marker auf der Karte. | [waypoint_marker.md](frontend/waypoint_marker.md) |
| **ImagePopup** | Zeigt Bild und Beschreibung in einem Popup mit Blur-Hintergrund. | [image_popup.md](frontend/image_popup.md) |
| **AdminLogin** | Login-Maske unter der Route `/wal`. | [admin_login.md](frontend/admin_login.md) |
| **AdminPanel** | Admin-Ansicht mit Klick-auf-Karte zum Platzieren von Wegpunkten. | [admin_panel.md](frontend/admin_panel.md) |
| **ImageUpload** | Dialog zum Hochladen eines Bildes mit Kurzbeschreibung. | [image_upload.md](frontend/image_upload.md) |
| **ApiClient** | Zentraler HTTP-Client für alle Backend-Aufrufe. | [api_client.md](frontend/api_client.md) |

---

### Backend-Komponenten (FastAPI)

```mermaid
graph TB
    subgraph "Backend Container – FastAPI / Python"
        GpxParser["📄 GpxParser<br/><i>GPX → GeoJSON</i>"]
        WaypointRouter["📍 WaypointRouter<br/><i>CRUD API</i>"]
        ImageRouter["🖼️ ImageRouter<br/><i>Upload & Serve</i>"]
        AuthRouter["🔐 AuthRouter<br/><i>Login & Token</i>"]
        DatabaseManager["💾 DatabaseManager<br/><i>SQLite Zugriff</i>"]
        InputSanitizer["🛡️ InputSanitizer<br/><i>Validierung</i>"]
    end

    subgraph "Externe Abhängigkeiten"
        DB[("SQLite<br/>data.db")]
        GpxFS["📁 GPX Storage"]
        ImgFS["📁 Image Storage"]
        EnvFile[".env<br/>ADMIN_PASSWORD"]
    end

    GpxParser -- "liest GPX-Dateien" --> GpxFS
    WaypointRouter -- "SQL Queries" --> DatabaseManager
    WaypointRouter -- "delegiert Upload" --> ImageRouter
    WaypointRouter -- "bereinigt Input" --> InputSanitizer
    WaypointRouter -- "prüft Auth" --> AuthRouter
    ImageRouter -- "speichert Bilder" --> ImgFS
    ImageRouter -- "bereinigt Input" --> InputSanitizer
    ImageRouter -- "prüft Auth" --> AuthRouter
    AuthRouter -- "liest Passwort" --> EnvFile
    DatabaseManager -- "CRUD" --> DB
```

| Komponente | Aufgabe | Datei |
|:---|:---|:---|
| **GpxParser** | Liest GPX-Dateien und konvertiert sie in GeoJSON. | [gpx_parser.md](backend/gpx_parser.md) |
| **WaypointRouter** | REST-Endpunkte für Wegpunkt-CRUD. | [waypoint_router.md](backend/waypoint_router.md) |
| **ImageRouter** | REST-Endpunkte für Bild-Upload und -Abruf. | [image_router.md](backend/image_router.md) |
| **AuthRouter** | REST-Endpunkt für Admin-Authentifizierung. | [auth_router.md](backend/auth_router.md) |
| **DatabaseManager** | SQLite-Verbindung, Schema-Setup und Query-Abstraktion. | [database_manager.md](backend/database_manager.md) |
| **InputSanitizer** | Bereinigung und Validierung aller eingehenden Daten. | [input_sanitizer.md](backend/input_sanitizer.md) |

---

### Datenbank & Dateisystem

| Komponente | Aufgabe | Datei |
|:---|:---|:---|
| **Schema** | Tabellendefinitionen und SQL DDL. | [schema.md](database/schema.md) |
| **GpxStorage** | Konvention für die GPX-Dateiablage. | [gpx_storage.md](filesystem/gpx_storage.md) |
| **ImageStorage** | Konvention für die Bild-Dateiablage. | [image_storage.md](filesystem/image_storage.md) |

---

## Gesamtübersicht – Container-übergreifende Kommunikation

```mermaid
graph LR
    subgraph "Frontend – Vue.js"
        ApiClient["🔗 ApiClient"]
    end

    subgraph "Backend – FastAPI"
        GpxParser["📄 GpxParser"]
        WaypointRouter["📍 WaypointRouter"]
        ImageRouter["🖼️ ImageRouter"]
        AuthRouter["🔐 AuthRouter"]
    end

    ApiClient -- "GET /api/route" --> GpxParser
    ApiClient -- "GET/POST/DELETE<br/>/api/waypoints" --> WaypointRouter
    ApiClient -- "POST /api/images<br/>GET /api/images/:file" --> ImageRouter
    ApiClient -- "POST /api/auth/login" --> AuthRouter
```
