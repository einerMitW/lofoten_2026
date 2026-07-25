# Text & Input Sanitizer

**Summary**: Sicherheitsmodul zur Sanitisierung von Benutzereingaben zur Vermeidung von XSS- und Code-Injection-Angriffen.

**Sources**: [[backend/utils/sanitizer.py]]

**Last updated**: 2026-07-25

---

Die Komponente `sanitizer` stellt Hilfsfunktionen bereit, um alle über Formulare oder APIs eingegebenen Freitexte zu bereinigen.

## Anwendungsbereiche

- **Wegepunkt-Beschreibungen**: Entfernt gefährliche HTML-Tags (z. B. `<script>`, `<iframe>`) aus Beschreibungen von Hütten oder Zeltplätzen.
- **Bildtitel & Kategorien**: Strippt Sonderzeichen und verhindernde Skript-Injektionen.

## Related pages
- [[router_waypoints]]
- [[router_images]]
