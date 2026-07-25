# View Home

**Summary**: Hauptansicht der Webanwendung mit Kartenanzeige, Wegepunktmarkern und Höhenprofil-Synchronisation.

**Sources**: [[frontend/src/views/HomeView.vue]]

**Last updated**: 2026-07-25

---

Die Komponente `view_home` verbindet die Kartenvisualisierung und das Höhenprofil in einem interaktiven Dashboard.

## Enthaltene Komponenten

- [[component_map_view]]: Rendert den Pfad, Wegepunkte und Fotomarker auf einer OpenStreetMap / Leaflet Karte.
- [[component_elevation_profile]]: Zeigt das Höhenprofil unterhalb der Karte an.
- [[component_image_popup]]: Zeigt bei Klick auf Fotomarker eine hochauflösende Vorschau.

## Interaktiver Scrubber-Sync
Fährt der Benutzer mit der Maus über das Höhenprofil, wird die aktuelle Distanz über Events an die Karte übermittelt und dort vom Laser-Scrubber-Marker hervorgehoben.

## Related pages
- [[component_map_view]]
- [[component_elevation_profile]]
- [[component_image_popup]]
- [[api_service]]
