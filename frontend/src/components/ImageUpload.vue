<template>
  <div class="modal-overlay" @click.self="cancel">
    <div class="glass-panel upload-card">
      <button class="close-btn" @click="cancel">&times;</button>
      
      <div class="meta-tag">NEUEN WEGPUNKT ANLEGEN</div>
      <h2>Foto & Story hochladen</h2>
      <p class="coords">📍 {{ coords?.lat.toFixed(4) }}° N, {{ coords?.lng.toFixed(4) }}° E</p>

      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label>Titel</label>
          <input type="text" v-model="title" placeholder="z. B. Bivouac Kvalvika" required class="input" />
        </div>

        <div class="form-group">
          <label>Kurzbeschreibung</label>
          <textarea v-model="description" rows="3" placeholder="Geschichten zum Wegpunkt..." class="input"></textarea>
        </div>

        <div class="form-group">
          <label>Foto auswählen</label>
          <input type="file" ref="fileInput" accept="image/jpeg,image/png,image/webp" required class="file-input" />
        </div>

        <div v-if="error" class="error-msg">{{ error }}</div>

        <div class="actions">
          <button type="button" class="cancel-btn" @click="cancel">ABBRECHEN</button>
          <button type="submit" class="submit-btn" :disabled="loading">
            {{ loading ? 'SPEICHERN...' : 'WEGPUNKT SPEICHERN' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { API } from '../services/api.js';

const props = defineProps({
  coords: Object,
  token: String
});

const emit = defineEmits(['saved', 'cancel']);

const title = ref('');
const description = ref('');
const fileInput = ref(null);
const loading = ref(false);
const error = ref('');

async function handleSubmit() {
  if (!fileInput.value || !fileInput.value.files[0]) {
    error.value = 'Bitte ein Bild auswählen';
    return;
  }

  error.value = '';
  loading.value = true;

  try {
    const file = fileInput.value.files[0];
    const imageRes = await API.uploadImage(file, props.token);

    const wpData = {
      title: title.value,
      description: description.value,
      lat: props.coords.lat,
      lng: props.coords.lng,
      image_path: imageRes.url
    };

    await API.createWaypoint(wpData, props.token);
    emit('saved');
  } catch (err) {
    error.value = 'Fehler beim Hochladen des Wegpunkts';
  } finally {
    loading.value = false;
  }
}

function cancel() {
  emit('cancel');
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(12px);
  z-index: 200;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.upload-card {
  width: 100%;
  max-width: 440px;
  padding: 24px 28px;
  position: relative;
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
}

.meta-tag {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  color: var(--accent);
  margin-bottom: 4px;
}

h2 {
  font-size: 1.3rem;
  margin-bottom: 4px;
}

.coords {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: var(--muted);
  margin-bottom: 16px;
}

.form-group {
  margin-bottom: 14px;
}

label {
  display: block;
  font-size: 0.75rem;
  color: var(--muted);
  margin-bottom: 4px;
}

.input {
  width: 100%;
  padding: 10px;
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid var(--border);
  border-radius: 6px;
  color: var(--fg);
  font-family: var(--font-main);
}

.file-input {
  width: 100%;
  color: var(--muted);
  font-size: 0.85rem;
}

.actions {
  display: flex;
  gap: 10px;
  margin-top: 18px;
}

.cancel-btn {
  flex: 1;
  padding: 10px;
  background: transparent;
  border: 1px solid var(--border);
  color: var(--muted);
  border-radius: 6px;
  cursor: pointer;
}

.submit-btn {
  flex: 2;
  padding: 10px;
  background: var(--accent);
  color: #fff;
  border: none;
  border-radius: 6px;
  font-weight: 700;
  cursor: pointer;
}

.error-msg {
  color: var(--accent);
  font-size: 0.8rem;
  margin-bottom: 10px;
}
</style>
