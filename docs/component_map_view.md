# Component Map View

**Summary**: Leaflet 2D-Kartenkomponente zur Visualisierung von Routen-Polylines, POI-Markern und Bild-Icons.

**Sources**: [[frontend/src/components/MapView.vue]]

**Last updated**: 2026-07-25

---

Die Komponente `component_map_view` kapsele die Leaflet.js Karten-Integration.

## Kernfunktionen

### Karten-Initialisierung & Tiles
Initialisiert die Leaflet-Karte mit OpenStreetMap Tile-Layer. Zentriert die Ansicht automatisch auf die Lofoten-Koordinaten.

### Routen-Rendering (`Polyline`)
Zeigt die aus [[router_gpx]] abgerufenen Trackpoints als farbige Polyline an.

### Marker-Integration
- **Wegepunkte**: Farbcodierte Marker je nach Kategorie (Hütte, Gipfel, Zeltplatz).
- **Fotopunkte**: Kamera-Icons, die bei Klick [[component_image_popup]] öffnen.

## Related pages
- [[component_scrubber_layer]]
- [[component_elevation_profile]]
- [[component_image_popup]]
- [[view_home]]
