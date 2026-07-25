# Test Infrastructure Frontend

**Summary**: Vitest & JSDOM Setup für isolierte Vue 3 Komponenten- und Integrationstests.

**Sources**: [[frontend/src/__tests__/setup.spec.js]], [[frontend/vite.config.js]]

**Last updated**: 2026-07-25

---

Die Komponente `test_infrastructure_frontend` steuert die Frontend-Testausführung.

## Test-Runner & Umgebung

### Vitest + JSDOM
Nutzt Vitest in einer nachgebildeten Browserumgebung (`jsdom`), um DOM-Interaktionen, Event-Handling und Komponenten-Rendering ohne echten Browser zu testen.

### Component Specs
Enthält Testdateien für zentrale Komponenten:
- `ElevationProfile.spec.js`: Testet Chart.js Rendering und Hover-Events.
- `ImagePopup.spec.js`: Testet Modal-Sichtbarkeit und Props-Übergabe.
- `MapView.spec.js`: Testet die Erstellung und Aktualisierung der Leaflet Scrubber Layergruppe.

## Related pages
- [[frontend_main]]
- [[component_map_view]]
- [[component_elevation_profile]]
