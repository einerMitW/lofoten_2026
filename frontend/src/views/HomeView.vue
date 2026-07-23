<template>
  <div class="home-view">
    <!-- Header HUD Panel -->
    <div class="glass-panel header-hud">
      <div class="title-section">
        <h1>LOFOTEN 2026</h1>
        <p class="subtitle">CROSSING THE ARCTIC TRAIL</p>
      </div>
    </div>

    <!-- Map View -->
    <MapView 
      :geojson="routeGeojson" 
      :waypoints="waypoints" 
      :scrubCoords="scrubCoords"
      @select-waypoint="openWaypoint"
    />

    <!-- Elevation Profile & Telemetry -->
    <ElevationProfile 
      :geojson="routeGeojson" 
      :telemetry="telemetry"
      @scrub="handleScrub"
    />

    <!-- Image Story Popup Modal -->
    <ImagePopup 
      v-if="selectedWaypoint" 
      :waypoint="selectedWaypoint"
      @close="selectedWaypoint = null"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import MapView from '../components/MapView.vue';
import ElevationProfile from '../components/ElevationProfile.vue';
import ImagePopup from '../components/ImagePopup.vue';
import { API } from '../services/api.js';

const routeGeojson = ref(null);
const telemetry = ref(null);
const waypoints = ref([]);
const scrubCoords = ref(null);
const selectedWaypoint = ref(null);

onMounted(async () => {
  try {
    const routeData = await API.getRoute();
    routeGeojson.value = routeData.geojson;
    telemetry.value = routeData.telemetry;

    waypoints.value = await API.getWaypoints();
  } catch (err) {
    console.error('Error loading trail data:', err);
  }
});

function handleScrub(coords) {
  scrubCoords.value = coords;
}

function openWaypoint(wp) {
  selectedWaypoint.value = wp;
}
</script>

<style scoped>
.home-view {
  width: 100vw;
  height: 100vh;
  position: relative;
  overflow: hidden;
}

.header-hud {
  position: absolute;
  top: 24px;
  left: 24px;
  z-index: 10;
  padding: 14px 20px;
}

h1 {
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: var(--fg);
}

.subtitle {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  color: var(--muted);
  letter-spacing: 0.08em;
}
</style>
