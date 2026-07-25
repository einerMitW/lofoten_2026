# Component Scrubber Layer

**Summary**: Dedizierte Leaflet Layer-Gruppe zur flackerfreien Darstellung des Laser-Scrubber-Markers auf der Karte.

**Sources**: [[frontend/src/components/MapView.vue]]

**Last updated**: 2026-07-25

---

Die Komponente `component_scrubber_layer` ist eine spezialisierte Sub-Struktur innerhalb von `MapView.vue`.

## Motivation & Problembehebung
Um Marker-Flackern und Performance-Einbußen bei schnellen Mausbewegungen auf dem Höhenprofil zu vermeiden, verwendet die Karte eine eigene Leaflet `L.layerGroup()` (`scrubberLayer`).

## Funktionsweise
Beim Empfang eines Hover-Events vom [[component_elevation_profile]] wird lediglich der Marker in `scrubberLayer` aktualisiert, anstatt die gesamte Karten-Polyline oder andere Marker neu zu zeichnen.

## Related pages
- [[component_map_view]]
- [[component_elevation_profile]]
