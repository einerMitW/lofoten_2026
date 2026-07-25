<template>
  <div class="modal-overlay">
    <div class="glass-panel login-card">
      <div class="meta-tag">ADMIN ACCESS GATEWAY</div>
      <h2>Authentifizierung</h2>
      <p class="subtitle">Bitte gib das Admin-Passwort ein, um den Editor freizuschalten.</p>

      <form @submit.prevent="handleSubmit">
        <input 
          type="password" 
          v-model="password" 
          placeholder="Admin Passwort..." 
          class="password-input"
          required
        />
        <div v-if="error" class="error-msg">{{ error }}</div>
        <button type="submit" class="submit-btn" :disabled="loading">
          {{ loading ? 'PRÜFE...' : 'ANMELDEN' }}
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { API } from '../services/api.js';

const emit = defineEmits(['authenticated']);

const password = ref('');
const error = ref('');
const loading = ref(false);

async function handleSubmit() {
  error.value = '';
  loading.value = true;
  try {
    const res = await API.login(password.value);
    emit('authenticated', res.token);
  } catch (err) {
    error.value = 'Ungültiges Admin-Passwort';
  } finally {
    loading.value = false;
  }
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

.login-card {
  width: 100%;
  max-width: 380px;
  padding: 28px 24px;
}

.meta-tag {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  font-weight: 700;
  color: var(--accent);
  letter-spacing: 0.1em;
  margin-bottom: 6px;
}

h2 {
  font-size: 1.5rem;
  margin-bottom: 6px;
}

.subtitle {
  font-size: 0.85rem;
  color: var(--muted);
  margin-bottom: 20px;
}

.password-input {
  width: 100%;
  padding: 12px;
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid var(--border);
  border-radius: 6px;
  color: var(--fg);
  font-family: var(--font-mono);
  margin-bottom: 14px;
}

.password-input:focus {
  outline: none;
  border-color: var(--accent);
}

.submit-btn {
  width: 100%;
  padding: 12px;
  background: var(--accent);
  color: #fff;
  border: none;
  border-radius: 6px;
  font-family: var(--font-mono);
  font-weight: 700;
  cursor: pointer;
}

.error-msg {
  color: var(--accent);
  font-size: 0.8rem;
  margin-bottom: 12px;
}
</style>
