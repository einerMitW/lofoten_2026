# InputSanitizer

| Eigenschaft | Wert |
|:---|:---|
| **Name** | InputSanitizer |
| **Container** | Backend (FastAPI) |
| **Sprache** | Python |

## Aufgabe
Zentrale Bereinigungsfunktionen für alle eingehenden Nutzereingaben, bevor diese in der Datenbank gespeichert oder vom System verarbeitet werden:

- **Textbereinigung:** Entfernt HTML-Tags, Script-Injections und unerwünschte Sonderzeichen aus Bildbeschreibungen.
- **Dateivalidierung:** Prüft den tatsächlichen MIME-Type hochgeladener Bilder (nicht nur die Dateiendung), um die Ausführung bösartiger Dateien zu verhindern.
- **Längenbegrenzung:** Limitiert die maximale Textlänge von Beschreibungen.

## Begründung
Auch wenn nur Admins Daten einfügen können, gilt das Prinzip "Trust No Input". Ein kompromittiertes Admin-Passwort oder ein unachtsamer Admin könnte schadhaften Input einschleusen. Der Sanitizer stellt sicher, dass **keine** Roheingabe ungefiltert ins System gelangt.

**Bezug:** developer_dialog.md, Abschnitt 7 (Unvertrauenswürdigkeit)

## Abhängigkeiten
- **Intern:**
  - Wird genutzt von → [WaypointRouter](waypoint_router.md) (Beschreibungen)
  - Wird genutzt von → [ImageRouter](image_router.md) (Dateivalidierung)
- **Libraries:** `bleach` oder ähnlich (HTML-Bereinigung)
