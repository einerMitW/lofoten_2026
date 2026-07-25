# Knowledge Graph Index

Willkommen im LLM-Wiki der Lofoten 2026 Webanwendung. Dieser Index verlinkt alle Systemkomponenten, Datenmodelle und Services als strukturierter Wissensgraph.

## Backend Komponente
- [[backend_main]]: FastAPI Einstiegspunkt, CORS & statischer Dateimount.
- [[backend_config]]: Laden von Umgebungsvariablen & Pfadkonfigurationen.
- [[database_engine]]: SQLite Datenbankverbindung & Session-Management.
- [[table_users]]: Schema der Benutzertabelle für Administratorzugänge.
- [[table_waypoints]]: Schema der Wegepunkttabelle für Etappen-POIs.
- [[table_route_points]]: Schema der Routenpunkttabelle für GPX-Trackpoints.
- [[table_images]]: Schema der Bildertabelle für Standortfotos.
- [[crud_waypoints]]: Datenbank-CRUD-Operationen für Wegepunkte.
- [[crud_route_points]]: Datenbank-CRUD-Operationen für Routenpunkte.
- [[crud_images]]: Datenbank-CRUD-Operationen für Bilder.
- [[crud_auth]]: Passwort-Hashing & Benutzer-Verifizierungslogik.
- [[router_auth]]: API-Endpunkte für Login & Token-Verifizierung.
- [[router_gpx]]: API-Endpunkte für GPX-Upload & Routenabruf.
- [[router_waypoints]]: API-Endpunkte für Wegepunkt-CRUD-Operationen.
- [[router_images]]: API-Endpunkte für Bild-Upload & Galerie-Verwaltung.
- [[gpx_parser_core]]: Kernlogik des GPX-Parsers mittels gpxpy.
- [[gpx_auto_alignment]]: Automatische Richtungsausrichtung von Etappen.
- [[gpx_metrics]]: Distanz- & Kumulierte Höhenmeter-Berechnung.
- [[sanitizer]]: HTML- & Input-Sanitisierungs-Utility.

## Frontend Komponente
- [[frontend_main]]: Vue 3 Hauptinstanz & Layout-Initialisierung.
- [[frontend_router]]: Vue-Router Konfiguration & Navigation.
- [[api_service]]: Axios HTTP-Client & Backend-Schnittstelle.
- [[view_home]]: Hauptansicht für Karte & Höhenprofil.
- [[view_admin]]: Administrations-Ansicht & Dashboard.
- [[component_map_view]]: Leaflet Kartenkomponente & Routendarstellung.
- [[component_scrubber_layer]]: Dedizierter Leaflet Scrubber-Marker Layer.
- [[component_elevation_profile]]: Chart.js Höhenprofil & Hover-Synchronisation.
- [[component_image_popup]]: Modal-Vorschaukomponente für Bilder.
- [[component_admin_login]]: Authentifizierungsformular für Administratoren.
- [[component_image_upload]]: Upload-Formular für Fotos.

## Architektur & Infrastructure
- [[test_infrastructure_backend]]: Pytest Testsuite, Fixtures & Isolation.
- [[test_infrastructure_frontend]]: Vitest & JSDOM Frontend-Test-Setup.
- [[c4_architecture_model]]: C4 System Context & Container Architektur.
- [[ci_backend_pipeline]]: GitHub Actions CI Workflow für Backend Pytest.
- [[ci_frontend_pipeline]]: GitHub Actions CI Workflow für Frontend Vitest.
- [[containerization_docker]]: Multi-Container Docker Setup mit HTTPS & Port 5567.
