
# Lofoten Trail Design System

**Ästhetische Richtung:** Arctic Tech / Dark Sage
**Stimmung:** Funktional, arktisch, hochpräzise. Ein tiefes, waldiges Türkis ("Dark Sage") trifft auf transluzente Glas-Elemente und extrem kontrastreiche, leuchtend rote Neon-Akzente. Das Interface fühlt sich wie ein professionelles Navigationsinstrument an.

---

## 1. Farb-Tokens & Anwendungsregeln

Das Farbsystem basiert auf strenger Monochromie im Hintergrund, um die Karte wirken zu lassen, und setzt Akzente sehr gezielt als Signalfarbe ein.

### Base & Surface (Hintergründe)
- **`--bg`** (`oklch(14% 0.015 185)` / `#0d1412`): 
  **Wann anwenden:** Ausschließlich für den absoluten Seitenhintergrund unter der Karte. Bildet den dunklen, fast schwarzen "Ozean"-Kontrast, auf dem die Landmassen plastisch hervortreten.
- **`--surface`** (`rgba(18, 28, 25, 0.75)`): 
  **Wann anwenden:** Für alle schwebenden UI-Panels (HUD, Höhenprofil, Overlays). Muss immer in Kombination mit `backdrop-filter: blur(16px)` verwendet werden, um den hochwertigen Glasmorphismus-Effekt zu erzielen.
- **`--surface-hover`** (`rgba(38, 66, 58, 0.85)`): 
  **Wann anwenden:** Für interaktive Flächen wie Hover-Zustände von Etappen-Buttons, Timeline-Controls oder klickbaren Listen-Elementen.

### Foreground (Texte & Linien)
- **`--fg`** (`oklch(95% 0.01 185)`):
  **Wann anwenden:** Primäre Textfarbe für Überschriften, Telemetrie-Werte und aktiven Text. Bietet maximalen Kontrast zum dunklen Hintergrund, ist aber minimal abgetönt (weicher als reines `#FFFFFF`), um die Augen nicht zu überanstrengen.
- **`--muted`** (`oklch(65% 0.02 185)`):
  **Wann anwenden:** Sekundärer Text für Labels, Kicker, Untertitel, Beschreibungen und Achsen-Einheiten. Sorgt für eine klare visuelle Hierarchie.
- **`--border`** (`rgba(255, 255, 255, 0.12)`):
  **Wann anwenden:** Für subtile Trennlinien zwischen Container-Sektionen, feine Panel-Rahmen (`border`) und X/Y-Gitterlinien im Höhenprofil.

### Accent (Signalfarben)
- **`--accent`** (`oklch(65% 0.22 25)` / `#ff4a5a`):
  **Wann anwenden:** Sehr sparsam! Das Neonrot ist der absolute Fokuspunkt. Wird ausschließlich für die tatsächliche Wanderroute (Line), den aktiven Laser-Scrubber, das "LIVE"-Badge und hervorgehobene Telemetrie-Highlights genutzt.
- **`--accent-glow`** (`rgba(255, 74, 90, 0.4)`):
  **Wann anwenden:** Für weiche Schatten (`box-shadow`) bei leuchtenden Elementen, wie dem Pulsieren des LIVE-Badges oder dem Schimmern um die schwebenden Wegpunkt-Pins (Diamanten).

---

## 2. Typografie-Regeln

Zwei Schriftfamilien teilen sich das Interface. Sie sind streng getrennt nach erzählendem Inhalt (Narration) und technischen Daten (Telemetrie).

### Inter (Display & Body)
- **Einsatzgebiet:** Titel, Fließtexte, längere Beschreibungen.
- **Regeln:**
  - **Headlines:** Eng gesetzt (`letter-spacing: -0.01em` bis `-0.02em`), um ein kompaktes, professionelles Erscheinungsbild zu erzielen.
  - **Rendering:** OS-Glättung zwingend aktivieren (`-webkit-font-smoothing: antialiased`).

### JetBrains Mono (Data & Telemetry)
- **Einsatzgebiet:** Zahlen, Messwerte, Diagramm-Labels, Kicker, Etappennamen, Achsenbeschriftungen.
- **Regeln:**
  - **Labels (Kicker):** Immer in Großbuchstaben (All-Caps) und mit deutlich erweiterter Laufweite (`letter-spacing: 0.08em` bis `0.1em`), Farbe: `--muted`.
  - **Zahlen (Telemetrie):** Zwingend `font-variant-numeric: tabular-nums` nutzen. Dies verhindert, dass Zahlen (z. B. Distanz `14.2 km` vs `14.8 km`) beim dynamischen Durchzählen und Scrubbing unruhig wackeln.

---

## 3. Core UI Components

### 3.1 Glassmorphism Panels
Die schwebenden Overlays (HUD links, Profil rechts) heben sich durch räumliche Tiefe ab, nicht durch deckende Hintergrundfarben.
```css
.glass-panel {
  background: var(--surface);
  backdrop-filter: blur(16px);
  border: 1px solid var(--border);
  border-radius: 8px;
  /* Feines, inneres Glanzlicht oben + tiefer, weicher Drop-Shadow */
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.05), 0 12px 32px rgba(0,0,0,0.4);
}
```

### 3.2 Telemetry Inlays
Die Karten für Live-Daten (Distanz, Höhe) sitzen innerhalb der Glass Panels. Sie werden abgedunkelt, um optisch tiefer im Panel zu liegen.
```css
.telemetry-card {
  background: rgba(0, 0, 0, 0.2); /* Subtiles Loch im Panel */
  border: 1px solid var(--border);
  padding: 10px;
  border-radius: 4px;
}
```

### 3.3 Status Pills ("LIVE")
Der leuchtende Indikator pulsiert sanft und suggeriert Echtzeit-Tracking.
```css
.status-pill {
  background: rgba(255, 74, 90, 0.15);
  color: var(--accent);
  border: 1px solid var(--accent);
  animation: pulseLive 2s infinite; /* Vergrößert und verkleinert den box-shadow */
}
```

### 3.4 Interactive Scrubber (SVG Chart)
Der Laser-Pointer, der über das Höhenprofil gleitet. 
- **Verhalten:** Muss weich per `opacity` ausblenden (`transition: opacity 0.15s ease-out`), wenn der Mauszeiger das Diagramm verlässt (kein plötzliches Aufploppen).
- **Gitter:** Die Gitterlinien der Y-Achse nutzen `stroke-dasharray: 3 4` für eine tech-affine Radar-Optik.

---

## 4. Map Engine Styling (Leaflet Filter)

Um herkömmliche, dunkelgraue Leaflet-Basiskarten (z.B. `CartoDB Dark Matter`) exakt in das atmosphärische, arktische Waldtürkis der UI einzufärben – ohne eigene Tilesets generieren zu müssen – wird dieser CSS-Matrix-Filter global auf die Kachelebene angewandt:

```css
.leaflet-tile-pane {
  /* Zieht Schwarz/Grau in ein helleres, kontrastreiches Waldtürkis (Dark Sage) */
  filter: sepia(1) hue-rotate(130deg) saturate(3) brightness(1.7) contrast(1.3);
}
```

---

## 5. Motion, Animation & A11y

Alle Animationen im Projekt sind funktional, physikalisch gedämpft und unterstützen zwingend Barrierefreiheit.

- **Eintritt (`fadeUp` / `fadeIn`):** Beim Laden faden Panels mit `transform: translateY(16px)` und einem weichen Easing (`cubic-bezier(0.2, 0, 0, 1)`) gestaffelt ein (HUD zuerst, dann Timeline, dann Profil). Die Karte blendet im Hintergrund weich per `opacity` ein, um Flackern (FOUM - Flash of Unstyled Map) zu verhindern.
- **Focus States (Tastatur):** Interaktive Flächen wie das Höhenprofil-Diagramm (`chart-hotspot`) haben einen `tabindex="0"`. Bei `:focus-visible` erscheint eine Outline mit Abstand (`outline-offset: 2px`) in `--accent`-Farbe.
- **Reduced Motion Fallback (`prefers-reduced-motion`):**
  Zwingend erforderlich. Nutzer mit OS-seitig reduzierter Bewegung dürfen keine Kamera-Flüge, fliegenden Panels oder pulsierenden Badges sehen.
  ```css
  @media (prefers-reduced-motion: reduce) {
    *, ::before, ::after {
      animation-duration: 0.01ms !important;
      transition-duration: 0.01ms !important;
      scroll-behavior: auto !important;
    }
  }
  ```
