# Component Elevation Profile

**Summary**: Chart.js Diagrammkomponente zur Darstellung des Höhenprofils mit interaktiver Hover-Synchronisation.

**Sources**: [[frontend/src/components/ElevationProfile.vue]]

**Last updated**: 2026-07-25

---

Die Komponente `component_elevation_profile` visualisiert den Höhenverlauf der Wanderung über die kumulierte Distanz.

## Diagramm-Integration (Chart.js)

### Datensätze
Trägt die Distanz in km auf der X-Achse und die Höhe in Metern auf der Y-Achse ab. Rendert ein sanft gefülltes Liniendiagramm.

### Hover-Events & Sync
Beim Bewegen des Mauszeigers über das Diagramm wird der nächstgelegene Koordinatenpunkt ermittelt und ein Event an [[component_map_view]] gesendet, um den [[component_scrubber_layer]] exakt an dieser Stelle auf der Karte anzuzeigen.

## Related pages
- [[component_map_view]]
- [[component_scrubber_layer]]
- [[view_home]]
