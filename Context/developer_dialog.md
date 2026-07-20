# Development Dialog
Software sollte Probleme lösen, intuitiv und leicht für den Anwender zu verstehen sein und dabei die Triade der Softwareentwicklung hochhalten: Modularität, Testbarkeit/Dokumentation und Skalierbarkeit.

Die folgenden Schritte sind ein Dialog des Entwicklers mit der Software.

Ziele des Dokuments sind:
- Nutzerzentrierte Entwicklung
- Fokus auf MVP und Kernfunktionen
- Festlegen der Grundzüge und Abwägung der Technologien
- Eingrenzen des Scopes: Was will ich, was will ich nicht?
- Iterative Entwicklung auf Grundlage eines MVP
  Für die einzelnen Entwicklungsschritte stellt man sich Fragen, um seine Ziele und Strategie dorthin genauer kennenzulernen. Es geht um einen inneren Dialog mit dem Produkt.

## Ist-Analyse
Kontext: 
Entwicklet werden soll eine Webapp welche einen Urlaub auf den Lofoten aufbereitet.
Die Webapp solle die Route der Lofotenüberquerung auf einer karte abbilden anhand dieser Bilder als Higlightpunkte als Popup plaziert werden könnnen.
Bilder sollen ihr Geschichte des Urlaubs als moderne Fotokolekiton im Kotext des Urlaubes eingebettet erzählen.

Wie werden Prozesse bisher behandelt?
- Man macht im Urlab bilder welche anschließend oft kontextlos und Chronologisch in der Galerie lieben bleiben.
Was sind vorhandene Tools oder Software?
- Handygalerie oder Autauschlaufwerke
Welche Welche Probleme gibt es damit?
- Bilder Liegen einfach nur unsichbar in der Galerie anstatt ihre geschiechte zu erzählen. 

## 1) Anforderungen
Was für ein Problem löst meine Anwendung?
- Das vergessen der besten Urlaubsmomente
- Bilder erzählen nun anschaulich ihre Geschichte
- Bilder bleiben dauerhaft leicht im netz zu erreichen und schön Präsenteirt 
Für wen ist meine Anwendung?
- Teilnehmer der Reise
Warum mache ich das Projekt?
- Um ein Artefakt aus dem urlaub zu erschaffen

Usecases: Als Anwender will ich ... tun, um ... Ziele zu erreichen.
1. Als Anwender will ich die Karte mit der eingezeichneten Route der Lofoten sehen, um die Reise nachfolziehen zu können.
2. Als Anwender will ich ein höhenprofiel sehen, um die Geodaten der Route zu erfahen.
3. Als Anwender will ich mit einem Klick auf markierte stellen ein Bilder Pop up öffnen, um mir Bilder anzusehne die an dieser Stelle der route geschossen wurden.
4. Als Admin will ich über die versteckte URL-Route `/wal` den Admin-Bereich aufrufen können, um eine Login-Maske zu erhalten.
5. Als Admin will ich nach dem Login durch Klick auf die Karte an der Stelle ein Popup haben, um Bilder mit kurzer Beschreibung als Wegpunkt hochzuladen.
6. Als Admin will ich, dass die hochgeladenen Bilder persisten Gespeichert werden sodass sie beim erneuten öffnen immer noch da sind.
6. Als Anwender will ich einen einfachen Onepager ohne scrollen und mit simplem Minimalistischer Ui um die Route wirken lassen zu können. 

Abuse Case und Evil User Behavior: Als Angreifer will ich ... tun, um ... .
1. Als Angreifer will ich das Admin Passwort brute forcen um zugriff zu erlangen. 
2. Als Angreifer will ich die Nezwerkpakte in den Devtools verwenden um eventuelle vertrauliche daten aus den Gesendeten Pakten auszulesen.

## 2) Datenmodell
Was sind meine Datenentitäten und welche Attribute haben sie?
- Gpx Datein: Name, Koordinaten
- Bilder: Kurzbeschreibung, Bildpfad (Pointer auf das Dateisystem), Koordinaten
- Admin: Passwort
Wie werden diese Daten erhoben?
- Gpx Datein werden in einem Ordner gespeichert auf den man Zugreifen kann.
- Bilder werden durch Admins hochgeladen. Das Backend speichert die Datei im Dateisystem und legt den Dateipfad als Referenz in der Datenbank ab.
- Admin ist jder der sich im Admin panel anmelden kann. Das Passwort wird in einer .env abgelegt.
Wie werde ich die Daten anwenden / abrufen?
- Die GPX Datein müssen ausgelsen werdne um die Route auf der Karte darzustellen.
- Bilder werden im Frontend gerendert sobald ein Popup geöffnent wird.
- Aus den Daten der GPX Datiein wird ein Höhenprofiel gerendert.
Wie interagieren die Daten untereinander?
- Untereinander nicht, da jede für sich im Frontend dargestellt wird.

## 3) MVP Idee
Ist das Feature wirklich eine Kernfunktion:
- Admin login
- Karten Darstellung (Mapbox)
- Umwandlung der GPX-Dateien in ein JSON/Array Format
- Skalieren und Mappen der Koordinaten-Daten auf die Mapbox Karte

Folgende Features nach der Erstimplementierung / Deployment:
- höhenprofiel
- korrektes Styling / Farbschema anwendung
- Eifügen von neunen Bildern
- Öffnen von Bildern im Popup

## 4) User Interaktion Design
- Welche Screens werden benötigt?
1. Home: Screen der beim Starten der Anwendung angezeigt wird. Er gibt das einseiteige Layout vor. Enthält karte, höhenprofiel kachel, Route auf der Karte, Bilder Wegpunkte.
2. Popup Bilder: öffnet ein Popup der mit dem Bild un der Kurzbeschreibung. Hintergurnd ins geblurred
3. Admin Screen (erreichbar über `/wal`): Ansicht des Admin, in dem er mit Klick auf die Karte einen Punkt platzieren kann, um den Bild-Upload zu starten.
4. Admin Bild einfügen: Kann bilder hochladen und diese mit Kurzbeschreibung versehen. Diese werden dann auf der Karte eingefügt. Gleiche Komponente wie das Popup Bilder mit geblurrtem hintergrund. 

## 5) Skala
Sollen echte Nutzer auf die Anwendung?
-  Ja
Wie viele Anwender sollen es werden?
- Zwichen 2 bis 10 
Ist es eine Studien-, Hobby-, Portfolio-Anwendung?
- Hobby Projekt
Verwende ich es in 1, 6, 12 Monaten noch?
- Ja im optimalfall wird die Anwendung einmal gehostet und man kann sie wieder zur erinnerung jeder Zeit weider aufrufen. Mindestzeitraum sind 6 Monate angedacht.

## 6) High Level Architektur
Welche generellen Container hat das System (Frontend, Backend, DB, ...)? (Am besten in einem C4-Modell)
- Frontend
- Backend
- GPX Datei Ablage (Dateisystem)
- Bilddateien Ablage (Dateisystem)
- Bilder-Metadaten speichern.

*Hinweis:* Backend und Frontend werden zunächst in eigenen Ordnern innerhalb desselben Projekts (Monorepo) entwickelt. Später sollen sie containerisierbar (Docker) gemacht werden.

Wie sieht die Kommunikation zwischen diesen Teilen aus (Wer muss mit wem verbunden werden)?
- Frontend mit Backend
- Backend mit DB und GPX Datein

Welches sind die kritischen Bestandteile meiner Architektur, ohne die die Applikation gar nicht läuft?
- Auslesender GPX im Backend.
- Rendern der Ausgelsenen GPX im Frontend.

----
**Bis hierhin waren alle Überlegungen nicht technisch.**
----
## 7) Sicherheit
Welche Angriffsvektoren gibt es nach STRIDE?

Least Privilege: Hat jede Komponente wirklich nur die minimal notwendigen Rechte auf die Daten?
- Ja, da nicht jeder die Anwendung verändern kann. 
- Nur das Backend kann Bilder aus der Bild db lesen, einfügen und bearbeiten.
- Das Backend kann die GPX datein nur auslesen und nicht beschreiben

Unvertrauenswürdigkeit: Wie behandelt das System Eingaben, die zwar syntaktisch korrekt, aber semantisch bösartig sind?
- Selbst im Admin modus müssen hochgeladene Bilder und Bildbeschreibungen duch bereinigungsfunktionen überprüft werden.
- Kein direkt übernahme in Query Statements

## 8) Datenminimierung & Rollenvergabe
Welche Daten müssen User von sich preisgeben?
- Garkein
Sind diese Daten personenbezogen und wie gehe ich damit um?
- Nein sind sie nicht, das man die seite Anonym verwenden kann.
- Selbst berechtiget Admins müssen nur ein Passwort aber keine Namen oder Personenbezogene Daten eingeben.
Wie kann ich das "Recht auf Vergessenwerden" auf den technischen Komponenten umsetzen?

Welche Rollen gibt es?
- User
- Admin
Wie werden diese Rollen an User vergeben?
- Durch kenntniss vom Passwort
Wie werden User Identifiziert?
- Garnicht. Sie bleiben anonyme Besucher.
Wie werden User Authentifiziert?
- Garnicht. Sie bleiben anonyme Besucher.
Wie stellt man sicher, dass die Rollenvergabe kein Single Point of Failure wird? 
- Systemadmins können das Passwort in den .env verändern und so das Passwort durch root access ändern.

## 9) Stack
Welche Tools kann ich für die einzelnen Container der Architektur verwenden (kurz begründet)?
- Frontend: **Vue.js** - Sehr intuitiv, leichtgewichtig und bietet eine tolle Komponentenstruktur für das UI.
- Karte: **Mapbox GL JS** für hervorragendes Styling, Vektor-Tiles und 3D-Fähigkeiten. GPX Dateien werden geparst und als JSON eingebunden.
- Bilder Speichern: Die Bilddateien liegen auf dem Dateisystem. Die Metadaten (Pfad, Koordinaten) liegen in einer **SQLite** Datenbank.
- Backend: **FastAPI (Python)** - Sehr modernes, extrem schnelles Python-Framework.
Wie arbeiten die einzelnen Tools zusammen (Technisch konkrete Kommunikation)?
- Frontend und Backend kommunizieren via asynchroner REST-API Calls (Fetch) über HTTP.
Wie kann ich die Anwendung deployen? --> Deployment Path 
- Backend und Frontend werden in eigenen Ordnern im gleichen Projekt aufgebaut. Später werden diese containerisiert (Docker) für ein einfaches Deployment.

  **Nach der Festlegung der Anwendungsfälle, Funktionen, Skala, Navigation, Datenminimierung, Datenschutz und der generellen Architektur kann man nun in die Entwicklung einsteigen**
## 10) Einstieg in die Entwicklung
1. Anlegen der Monorepo-Ordnerstruktur (z.B. `/frontend` und `/backend`).
2. Festlegen von Entwicklungsmaximen: Sprache, Commit- und Branch-Conventions, KISS, Clean Code, ...
3. Proof of Concept: Vue.js mit Mapbox aufsetzen, GPX-Dateien in JSON/Array parsen und die Route korrekt skaliert und gemappt auf der Karte zeichnen.
4. Aufsetzen der Datenstruktur (SQLite) und des FastAPI Backends.
5. Aufsetzen eines User Story Backlogs mit Kanban-Board zum Projektmanagement.

## 11) Iterative Weiterentwicklung
Ab der Implementierung des MVP und dessen Deployment können weitere Features hinzugefügt werden, die in 3. gestrichen wurden.