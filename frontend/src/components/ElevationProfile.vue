<template>
  <div class="glass-panel profile-container" tabindex="0" @mouseleave="onMouseLeave">
    <div class="profile-header">
      <div class="header-title">
        <span class="kicker">HÖHENPROFIL & TELEMETRIE</span>
      </div>
      <div class="status-pill">
        <span class="status-dot"></span>
        LIVE TRACKING
      </div>
    </div>

    <!-- Compact Telemetry Cards Row -->
    <div class="metrics-row">
      <div class="telemetry-card">
        <span class="label">DISTANZ</span>
        <span class="value">{{ totalDist.toFixed(1) }} <span class="unit">km</span></span>
      </div>
      <div class="telemetry-card">
        <span class="label">HÖHENMETER</span>
        <span class="value">+{{ (telemetry?.elevation_gain || 0).toFixed(0) }} <span class="unit">m</span></span>
      </div>
      <div class="telemetry-card">
        <span class="label">MAX. HÖHE</span>
        <span class="value">{{ maxEle.toFixed(0) }} <span class="unit">m</span></span>
      </div>
      <div class="telemetry-card">
        <span class="label">MIN. HÖHE</span>
        <span class="value">{{ minEle.toFixed(0) }} <span class="unit">m</span></span>
      </div>
    </div>

    <!-- SVG Elevation Chart with Axes -->
    <div class="chart-wrapper" ref="chartWrapper" @mousemove="onMouseMove">
      <svg class="elevation-svg" viewBox="0 0 500 160" preserveAspectRatio="none">
        <defs>
          <linearGradient id="chartGradient" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#ff4a5a" stop-opacity="0.45"/>
            <stop offset="100%" stop-color="#ff4a5a" stop-opacity="0.02"/>
          </linearGradient>
        </defs>

        <!-- Y-Axis Grid & Labels -->
        <g class="y-axis">
          <line x1="35" y1="20" x2="495" y2="20" stroke="rgba(255,255,255,0.08)" stroke-dasharray="3 4"/>
          <text x="30" y="24" class="axis-label" text-anchor="end">{{ maxEle.toFixed(0) }}m</text>

          <line x1="35" y1="75" x2="495" y2="75" stroke="rgba(255,255,255,0.08)" stroke-dasharray="3 4"/>
          <text x="30" y="79" class="axis-label" text-anchor="end">{{ ((maxEle + minEle) / 2).toFixed(0) }}m</text>

          <line x1="35" y1="130" x2="495" y2="130" stroke="rgba(255,255,255,0.08)" stroke-dasharray="3 4"/>
          <text x="30" y="134" class="axis-label" text-anchor="end">{{ minEle.toFixed(0) }}m</text>
        </g>

        <!-- X-Axis Grid & Labels -->
        <g class="x-axis">
          <line x1="35" y1="135" x2="495" y2="135" stroke="rgba(255,255,255,0.15)"/>
          <text x="35" y="152" class="axis-label" text-anchor="start">0 km</text>
          <text x="265" y="152" class="axis-label" text-anchor="middle">{{ (totalDist / 2).toFixed(0) }} km</text>
          <text x="495" y="152" class="axis-label" text-anchor="end">{{ totalDist.toFixed(0) }} km</text>
        </g>

        <!-- Elevation Area & Line Path -->
        <path :d="areaPath" fill="url(#chartGradient)" />
        <path :d="linePath" fill="none" stroke="#ff4a5a" stroke-width="2" />

        <!-- Laser Scrubber Line -->
        <line v-if="scrubberX !== null" :x1="scrubberX" y1="15" :x2="scrubberX" y2="135" stroke="#ffffff" stroke-width="1.5" />
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

const totalDist = computed(() => props.telemetry?.total_distance_km || 100.0);
const maxEle = computed(() => props.telemetry?.max_elevation || 500.0);
const minEle = computed(() => props.telemetry?.min_elevation || 0.0);

const svgPoints = computed(() => {
  if (coordinates.value.length === 0) return [];
  const maxH = maxEle.value > 0 ? maxEle.value : 500;
  const minH = minEle.value;
  const rangeH = (maxH - minH) || 1;
  const totalD = totalDist.value || 1;

  return coordinates.value.map(c => {
    const ele = c[2] || 0;
    const cumDist = c[3] !== undefined ? c[3] : 0;
    
    // Plot X along chart width (35px to 495px margin for Y-axis)
    const x = 35 + (cumDist / totalD) * 460;
    // Plot Y vertically (20px to 130px)
    const y = 130 - ((ele - minH) / rangeH) * 110;
    return { x, y, coords: c, cumDist };
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
  return `${linePath.value} L 495 135 L 35 135 Z`;
});

function onMouseMove(e) {
  if (!chartWrapper.value || svgPoints.value.length === 0) return;
  const rect = chartWrapper.value.getBoundingClientRect();
  
  // Account for the 35px Y-axis margin inside the SVG (35px start, 460px plot width)
  const leftMargin = (35 / 500) * rect.width;
  const plotWidth = (460 / 500) * rect.width;
  
  const chartMouseX = Math.max(0, Math.min(e.clientX - rect.left - leftMargin, plotWidth));
  const ratio = chartMouseX / plotWidth;

  const targetDist = ratio * totalDist.value;
  
  // Find point with cumulative distance closest to targetDist
  let closestPoint = svgPoints.value[0];
  let minDiff = Math.abs(closestPoint.cumDist - targetDist);
  
  for (let i = 1; i < svgPoints.value.length; i++) {
    const diff = Math.abs(svgPoints.value[i].cumDist - targetDist);
    if (diff < minDiff) {
      minDiff = diff;
      closestPoint = svgPoints.value[i];
    }
  }

  if (closestPoint) {
    scrubberX.value = closestPoint.x;
    emit('scrub', closestPoint.coords);
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
  width: 520px;
  padding: 14px 18px;
  z-index: 10;
}

.profile-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.kicker {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: var(--muted);
}

.metrics-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 8px;
  margin-bottom: 10px;
}

.telemetry-card {
  padding: 6px 8px;
  display: flex;
  flex-direction: column;
}

.label {
  font-size: 0.6rem;
  color: var(--muted);
  letter-spacing: 0.06em;
  margin-bottom: 2px;
}

.value {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--fg);
}

.unit {
  font-size: 0.7rem;
  color: var(--muted);
  font-weight: 400;
}

.chart-wrapper {
  height: 160px;
  width: 100%;
  cursor: crosshair;
  position: relative;
}

.elevation-svg {
  width: 100%;
  height: 100%;
  overflow: visible;
}

.axis-label {
  font-family: var(--font-mono);
  font-size: 10px;
  fill: var(--muted);
}
</style>
