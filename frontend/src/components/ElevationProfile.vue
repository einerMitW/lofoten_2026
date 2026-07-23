<template>
  <div class="glass-panel profile-container" tabindex="0" @mouseleave="onMouseLeave">
    <div class="profile-header">
      <span class="kicker">HÖHENPROFIL & TELEMETRIE</span>
      <div class="status-pill">
        <span class="status-dot"></span>
        LIVE TRACKING
      </div>
    </div>

    <div class="metrics-grid">
      <div class="telemetry-card">
        <div class="label">DISTANZ</div>
        <div class="value">{{ telemetry?.total_distance_km || 0 }} <span class="unit">km</span></div>
      </div>
      <div class="telemetry-card">
        <div class="label">HÖHENMETER</div>
        <div class="value">+{{ telemetry?.elevation_gain || 0 }} <span class="unit">m</span></div>
      </div>
      <div class="telemetry-card">
        <div class="label">MAX. HÖHE</div>
        <div class="value">{{ telemetry?.max_elevation || 0 }} <span class="unit">m</span></div>
      </div>
    </div>

    <!-- SVG Elevation Chart -->
    <div class="chart-wrapper" ref="chartWrapper" @mousemove="onMouseMove">
      <svg class="elevation-svg" viewBox="0 0 500 120" preserveAspectRatio="none">
        <defs>
          <linearGradient id="chartGradient" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#ff4a5a" stop-opacity="0.4"/>
            <stop offset="100%" stop-color="#ff4a5a" stop-opacity="0.0"/>
          </linearGradient>
        </defs>

        <!-- Grid Lines -->
        <line x1="0" y1="30" x2="500" y2="30" stroke="rgba(255,255,255,0.08)" stroke-dasharray="3 4"/>
        <line x1="0" y1="70" x2="500" y2="70" stroke="rgba(255,255,255,0.08)" stroke-dasharray="3 4"/>

        <!-- Area & Line -->
        <path :d="areaPath" fill="url(#chartGradient)" />
        <path :d="linePath" fill="none" stroke="#ff4a5a" stroke-width="2" />

        <!-- Laser Scrubber Line -->
        <line v-if="scrubberX !== null" :x1="scrubberX" y1="0" :x2="scrubberX" y2="120" stroke="#ffffff" stroke-width="1.5" />
      </svg>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  geojson: Object,
  telemetry: Object
});

const emit = defineEmits(['scrub']);

const chartWrapper = ref(null);
const scrubberX = ref(null);

const coordinates = computed(() => {
  if (!props.geojson || !props.geojson.features) return [];
  const coords = [];
  props.geojson.features.forEach(feat => {
    if (feat.geometry && feat.geometry.coordinates) {
      coords.push(...feat.geometry.coordinates);
    }
  });
  return coords;
});

const svgPoints = computed(() => {
  if (coordinates.value.length === 0) return [];
  const count = coordinates.value.length;
  let maxEle = 0;
  coordinates.value.forEach(c => {
    if (c[2] > maxEle) maxEle = c[2];
  });
  if (maxEle === 0) maxEle = 500;

  return coordinates.value.map((c, i) => {
    const x = (i / (count - 1)) * 500;
    const y = 110 - ((c[2] / maxEle) * 95);
    return { x, y, coords: c };
  });
});

const linePath = computed(() => {
  if (svgPoints.value.length === 0) return '';
  return svgPoints.value.reduce((acc, pt, i) => {
    return `${acc} ${i === 0 ? 'M' : 'L'} ${pt.x.toFixed(1)} ${pt.y.toFixed(1)}`;
  }, '');
});

const areaPath = computed(() => {
  if (svgPoints.value.length === 0) return '';
  return `${linePath.value} L 500 120 L 0 120 Z`;
});

function onMouseMove(e) {
  if (!chartWrapper.value || svgPoints.value.length === 0) return;
  const rect = chartWrapper.value.getBoundingClientRect();
  const mouseX = Math.max(0, Math.min(e.clientX - rect.left, rect.width));
  const ratio = mouseX / rect.width;
  
  scrubberX.value = ratio * 500;
  
  const index = Math.floor(ratio * (svgPoints.value.length - 1));
  const selectedPoint = svgPoints.value[index];
  if (selectedPoint) {
    emit('scrub', selectedPoint.coords);
  }
}

function onMouseLeave() {
  scrubberX.value = null;
  emit('scrub', null);
}
</script>

<style scoped>
.profile-container {
  position: absolute;
  bottom: 24px;
  right: 24px;
  width: 440px;
  padding: 16px 20px;
  z-index: 10;
}

.profile-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 14px;
}

.kicker {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: var(--muted);
}

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  margin-bottom: 14px;
}

.label {
  font-size: 0.65rem;
  color: var(--muted);
  letter-spacing: 0.08em;
  margin-bottom: 4px;
}

.value {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--fg);
}

.unit {
  font-size: 0.75rem;
  color: var(--muted);
  font-weight: 400;
}

.chart-wrapper {
  height: 90px;
  width: 100%;
  cursor: crosshair;
  position: relative;
}

.elevation-svg {
  width: 100%;
  height: 100%;
  overflow: visible;
}
</style>
