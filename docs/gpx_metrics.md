# GPX Metrics Calculation

**Summary**: Algorithmen zur mathematischen Berechnung kumulierter Distanzen und Höhenmeter entlang der Route.

**Sources**: [[backend/utils/gpx_parser.py]]

**Last updated**: 2026-07-25

---

Die Komponente `gpx_metrics` berechnet aus den Geokoordinaten fortlaufende Metriken für das Höhenprofil.

## Haversine-Formel & Kumulierte Distanz
Die Entfernung zwischen zwei aufeinanderfolgenden Koordinaten $(lat_1, lon_1)$ und $(lat_2, lon_2)$ wird mittels der Haversine-Formel auf der Erdkugel berechnet:
$$d = 2r \arcsin\left(\sqrt{\sin^2\left(\frac{\Delta \phi}{2}\right) + \cos(\phi_1)\cos(\phi_2)\sin^2\left(\frac{\Delta \lambda}{2}\right)}\right)$$

Die kumulierte Distanz `cumulative_distance` summiert diese Teilstrecken fortlaufend auf.

## Kumulierter Höhengewinn/Verlust
Das Modul errechnet durch Aufsummieren positiver Höhenunterschiede den Gesamtanstieg sowie den Gesamtabstieg der Etappe.

## Related pages
- [[gpx_parser_core]]
- [[gpx_auto_alignment]]
- [[table_route_points]]
