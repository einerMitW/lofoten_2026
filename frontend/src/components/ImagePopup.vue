<template>
  <div v-if="waypoint" class="modal-overlay" @click.self="close">
    <div class="glass-panel popup-card">
      <button class="close-btn" @click="close">&times;</button>
      
      <div v-if="waypoint.image_path" class="image-wrapper">
        <img :src="waypoint.image_path" :alt="waypoint.title" class="popup-img" />
      </div>

      <div class="content-body">
        <div class="meta-tag">WEGPUNKT HIGHLIGHT</div>
        <h2 class="title">{{ waypoint.title }}</h2>
        <p v-if="waypoint.description" class="description">{{ waypoint.description }}</p>

        <div class="coords-info">
          📍 {{ waypoint.lat.toFixed(4) }}° N, {{ waypoint.lng.toFixed(4) }}° E
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  waypoint: Object
});

const emit = defineEmits(['close']);

function close() {
  emit('close');
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.65);
  backdrop-filter: blur(8px);
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.popup-card {
  width: 100%;
  max-width: 480px;
  overflow: hidden;
  position: relative;
  animation: fadeUp 0.25s cubic-bezier(0.2, 0, 0, 1);
}

.close-btn {
  position: absolute;
  top: 12px;
  right: 16px;
  background: none;
  border: none;
  color: var(--fg);
  font-size: 1.8rem;
  cursor: pointer;
  z-index: 10;
  line-height: 1;
}

.image-wrapper {
  width: 100%;
  max-height: 280px;
  overflow: hidden;
  background: #000;
}

.popup-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.content-body {
  padding: 20px 24px;
}

.meta-tag {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  color: var(--accent);
  letter-spacing: 0.1em;
  margin-bottom: 6px;
}

.title {
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--fg);
  margin-bottom: 8px;
}

.description {
  font-size: 0.9rem;
  color: var(--muted);
  line-height: 1.5;
  margin-bottom: 16px;
}

.coords-info {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--muted);
  border-top: 1px solid var(--border);
  padding-top: 10px;
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
