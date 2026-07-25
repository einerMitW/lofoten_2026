<template>
  <div class="admin-view">
    <AdminLogin v-if="!token" @authenticated="onAuthenticated" />

    <template v-else>
      <div class="glass-panel admin-hud">
        <div class="title-section">
          <div class="meta">ADMIN EDITOR MODUS</div>
          <h2>LOFOTEN 2026</h2>
          <p class="instruction">Klicke auf die Karte zum Platzieren oder auf einen Marker zum Löschen.</p>
        </div>
        <button class="logout-btn" @click="token = null">ABMELDEN</button>
      </div>

      <MapView 
        :geojson="routeGeojson" 
        :waypoints="waypoints"
        :adminMode="true"
        @map-click="handleMapClick"
        @select-waypoint="openWaypoint"
      />

      <ImageUpload 
        v-if="clickCoords"
        :coords="clickCoords"
        :token="token"
        @saved="onWaypointSaved"
        @cancel="clickCoords = null"
      />

      <ImagePopup 
        v-if="selectedWaypoint"
        :waypoint="selectedWaypoint"
        :isAdmin="true"
        @close="selectedWaypoint = null"
        @delete="handleDeleteWaypoint"
      />
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import MapView from '../components/MapView.vue';
import AdminLogin from '../components/AdminLogin.vue';
import ImageUpload from '../components/ImageUpload.vue';
import ImagePopup from '../components/ImagePopup.vue';
import { API } from '../services/api.js';

const token = ref(null);
const routeGeojson = ref(null);
const waypoints = ref([]);
const clickCoords = ref(null);
const selectedWaypoint = ref(null);

onMounted(async () => {
  try {
    const routeData = await API.getRoute();
    routeGeojson.value = routeData.geojson;
    waypoints.value = await API.getWaypoints();
  } catch (err) {
    console.error('Error loading data:', err);
  }
});

function onAuthenticated(t) {
  token.value = t;
}

function handleMapClick(coords) {
  if (token.value && !selectedWaypoint.value) {
    clickCoords.value = coords;
  }
}

function openWaypoint(wp) {
  selectedWaypoint.value = wp;
}

async function onWaypointSaved() {
  clickCoords.value = null;
  waypoints.value = await API.getWaypoints();
}

async function handleDeleteWaypoint(id) {
  try {
    await API.deleteWaypoint(id, token.value);
    selectedWaypoint.value = null;
    waypoints.value = await API.getWaypoints();
  } catch (err) {
    console.error('Failed to delete waypoint:', err);
  }
}
</script>

<style scoped>
.admin-view {
  width: 100vw;
  height: 100vh;
  position: relative;
  overflow: hidden;
}

.admin-hud {
  position: absolute;
  top: 24px;
  left: 24px;
  z-index: 10;
  padding: 16px 22px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 20px;
}

.meta {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  color: var(--accent);
  letter-spacing: 0.08em;
}

h2 {
  font-size: 1.1rem;
}

.instruction {
  font-size: 0.8rem;
  color: var(--muted);
}

.logout-btn {
  padding: 6px 12px;
  background: transparent;
  border: 1px solid var(--border);
  color: var(--muted);
  font-family: var(--font-mono);
  font-size: 0.75rem;
  border-radius: 4px;
  cursor: pointer;
}
</style>
