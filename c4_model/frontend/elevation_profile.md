# ElevationProfile

| Eigenschaft | Wert |
|:---|:---|
| **Name** | ElevationProfile |
| **Container** | Frontend (Vue.js) |
| **Sprache** | JavaScript / Vue.js SFC |

## Aufgabe
Rendert ein interaktives Höhenprofil der Route als Diagramm (z.B. mit Canvas oder einer Chart-Library). Zeigt die Höhenmeter über die Strecke hinweg an und ermöglicht es, durch Hover die aktuelle Position auf der Karte zu sehen.

## Begründung
Das Höhenprofil gibt dem Anwender die Möglichkeit, die Geodaten der Route zu erfahren und die Topografie der Lofotenüberquerung visuell nachzuvollziehen. Es ist ein Feature, das nach dem MVP implementiert wird, aber architektonisch bereits vorgesehen sein muss.

**User Story Bezug:** UC-2 (Höhenprofil sehen)

> **Hinweis:** Dieses Feature ist **Post-MVP** und wird erst nach der Erstimplementierung umgesetzt.

## Abhängigkeiten
- **Intern:**
  - Empfängt Höhendaten (Elevation-Array) von → [RouteLayer](route_layer.md)
  - Kann bei Hover die Position auf der Karte aktualisieren über → [MapView](map_view.md)
