# Frontend API Service

**Summary**: Axios HTTP-Client Service-Schicht für alle Asynchronen Backend-Aufrufe und Token-Verwaltung.

**Sources**: [[frontend/src/services/api.js]]

**Last updated**: 2026-07-25

---

Die Komponente `api_service` kapselt die Netzwerkkommunikation zwischen dem Vue Frontend und den REST-Endpunkten des FastAPIs.

## Funktionen

### Axios Instanz & Interceptors
Konfiguriert den Basis-URL (`/api`) und fügt bei vorhandenem JWT-Token automatisch den `Authorization: Bearer <token>` Header für geschützte Anfragen hinzu.

### Service-Methoden
- `getRoutePoints()`: Ruft Routendaten von [[router_gpx]] ab.
- `getWaypoints()`, `createWaypoint()`, `deleteWaypoint()`: Wegepunkt-Interaktionen mit [[router_waypoints]].
- `getImages()`, `uploadImage()`, `deleteImage()`: Bilderverwaltung mit [[router_images]].
- `login()`, `verifyToken()`: Authentifizierung mit [[router_auth]].

## Related pages
- [[router_auth]]
- [[router_gpx]]
- [[router_waypoints]]
- [[router_images]]
