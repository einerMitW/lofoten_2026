# GPX Stage Auto Alignment

**Summary**: Automatischer Algorithmus zur Erkennung und Invertierung umgekehrt aufgezeichneter GPX-Etappen.

**Sources**: [[backend/utils/gpx_parser.py]]

**Last updated**: 2026-07-25

---

Die Komponente `gpx_auto_alignment` löst das Problem von Etappen, die versehentlich entgegen der Hauptlaufrichtung (von Moskenesøya nach Austvågøya) aufgezeichnet wurden.

## Funktionsweise

### Distanzvergleich
Beim Hinzufügen einer neuen GPX-Etappe vergleicht der Algorithmus die Distanz des Start- und Endpunkts der neuen Etappe zum Endpunkt der vorherigen Etappe:
- Wenn `dist(end_point, prev_last) < dist(start_point, prev_last)` gilt, wurde die Etappe in umgekehrter Richtung aufgezeichnet.

### Punktreihenfolge Invertieren
Bei Auslösen des Kriteriums wird die Punkteliste der Etappe mittels `points.reverse()` invertiert, sodass der Routenverlauf durchgehend monoton in Hauptrichtung verläuft.

## Related pages
- [[gpx_parser_core]]
- [[gpx_metrics]]
- [[router_gpx]]
