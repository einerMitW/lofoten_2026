# GpxParser

| Eigenschaft | Wert |
|:---|:---|
| **Name** | GpxParser |
| **Container** | Backend (FastAPI) |
| **Sprache** | Python |

## Aufgabe
Liest GPX-Dateien aus dem [GpxStorage](../filesystem/gpx_storage.md)-Verzeichnis ein und konvertiert sie in ein GeoJSON-Format (Feature Collection). Die Konvertierung extrahiert:
- **Koordinaten-Array** (`[lng, lat]` Paare) für die Routenlinie.
- **Höhendaten-Array** (`elevation` pro Punkt) für das Höhenprofil.

Stellt einen REST-Endpunkt bereit: `GET /api/route` → GeoJSON Response.

## Begründung
GPX ist ein XML-basiertes Format, das Mapbox GL JS nicht nativ unterstützt. Die Konvertierung zu GeoJSON ist zwingend notwendig, damit das Frontend die Route rendern kann. Diese Logik liegt im Backend, weil:
1. Das Backend die GPX-Dateien bereits im Dateisystem hat.
2. Die Konvertierung nur einmal pro Datei stattfinden muss (Caching möglich).
3. Das Frontend nicht mit XML-Parsing belastet wird.

**User Story Bezug:** UC-1 (Route sehen), UC-2 (Höhenprofil)
**Kritischer Pfad:** Ja – ohne diese Komponente funktioniert die gesamte Anwendung nicht.

## Abhängigkeiten
- **Intern:**
  - Liest GPX-Dateien aus → [GpxStorage](../filesystem/gpx_storage.md)
  - GeoJSON wird konsumiert von → [RouteLayer](../frontend/route_layer.md) (Frontend)
  - Höhendaten werden konsumiert von → [ElevationProfile](../frontend/elevation_profile.md) (Frontend)
- **Libraries:** `gpxpy` (Python GPX-Parser)
