<template>
  <div id="map-container" ref="mapContainer"></div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

const props = defineProps({
  geojson: Object,
  waypoints: Array,
  scrubCoords: Array,
  adminMode: Boolean
});

const emit = defineEmits(['select-waypoint', 'map-click']);

const mapContainer = ref(null);
let map = null;
let routeLayer = null;
let markersLayer = null;
let scrubberLayer = null;
let scrubberMarker = null;
let initialFitDone = false;

onMounted(() => {
  if (!mapContainer.value) return;

  map = L.map(mapContainer.value, {
    zoomControl: false,
    attributionControl: false
  }).setView([68.0, 13.5], 9);

  L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
    maxZoom: 19,
    subdomains: 'abcd'
  }).addTo(map);

  markersLayer = L.layerGroup().addTo(map);
  scrubberLayer = L.layerGroup().addTo(map);

  map.on('click', (e) => {
    emit('map-click', { lat: e.latlng.lat, lng: e.latlng.lng });
  });

  if (props.geojson) renderRoute(props.geojson);
  if (props.waypoints) renderWaypoints(props.waypoints);
});

function renderRoute(geojson) {
  if (!map || !geojson) return;
  if (routeLayer) map.removeLayer(routeLayer);

  routeLayer = L.geoJSON(geojson, {
    style: {
      color: '#ff4a5a',
      weight: 3.5,
      opacity: 0.95,
      lineCap: 'round',
      lineJoin: 'round'
    }
  }).addTo(map);

  if (!initialFitDone && routeLayer.getBounds().isValid()) {
    map.fitBounds(routeLayer.getBounds(), { padding: [40, 40] });
    initialFitDone = true;
  }
}

function renderWaypoints(waypoints) {
  if (!map || !markersLayer) return;
  markersLayer.clearLayers();

  waypoints.forEach(wp => {
    const customIcon = L.divIcon({
      className: 'diamond-marker',
      iconSize: [16, 16],
      iconAnchor: [8, 8]
    });

    const marker = L.marker([wp.lat, wp.lng], { icon: customIcon });
    marker.on('click', () => emit('select-waypoint', wp));
    markersLayer.addLayer(marker);
  });
}

watch(() => props.geojson, (newVal) => renderRoute(newVal));
watch(() => props.waypoints, (newVal) => renderWaypoints(newVal), { deep: true });

watch(() => props.scrubCoords, (coords) => {
  if (!map || !scrubberLayer) return;
  if (!coords || coords.length < 2) {
    scrubberLayer.clearLayers();
    scrubberMarker = null;
    return;
  }
  const [lng, lat] = coords;
  if (!scrubberMarker) {
    scrubberMarker = L.circleMarker([lat, lng], {
      radius: 7,
      color: '#ffffff',
      fillColor: '#ff4a5a',
      fillOpacity: 1,
      weight: 2
    });
    scrubberLayer.addLayer(scrubberMarker);
  } else {
    scrubberMarker.setLatLng([lat, lng]);
  }
});
</script>

<style scoped>
#map-container {
  width: 100%;
  height: 100vh;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
}
</style>
