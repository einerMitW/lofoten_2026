# Component Image Popup

**Summary**: Modal-Dialog zur Anzeige hochauflösender Fotos und zugehöriger Wegepunkt-Informationen.

**Sources**: [[frontend/src/components/ImagePopup.vue]]

**Last updated**: 2026-07-25

---

Die Komponente `component_image_popup` stellt eine Lightbox-Vorschau für Fotomarker bereit.

## Funktionsweise

- Auslöser: Klick auf ein Foto-Icon auf der [[component_map_view]].
- Anzeige: Zeigt das hochauflösende Bild aus `/static/images`, den Bildtitel, die Geokoordinaten und den verknüpften Wegepunkt.
- Bedienung: Schließen über Button, Escape-Taste oder Klick außerhalb des Modals.

## Related pages
- [[component_map_view]]
- [[router_images]]
- [[view_home]]
