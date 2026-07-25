export const API = {
  async getRoute() {
    const res = await fetch('/api/route');
    if (!res.ok) throw new Error('Failed to fetch route');
    return res.json();
  },

  async getWaypoints() {
    const res = await fetch('/api/waypoints');
    if (!res.ok) throw new Error('Failed to fetch waypoints');
    return res.json();
  },

  async login(password) {
    const res = await fetch('/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ password })
    });
    if (!res.ok) throw new Error('Authentication failed');
    return res.json();
  },

  async uploadImage(file, token) {
    const formData = new FormData();
    formData.append('file', file);

    const res = await fetch('/api/images', {
      method: 'POST',
      headers: { 'Authorization': `Bearer ${token}` },
      body: formData
    });
    if (!res.ok) throw new Error('Image upload failed');
    return res.json();
  },

  async createWaypoint(data, token) {
    const res = await fetch('/api/waypoints', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(data)
    });
    if (!res.ok) throw new Error('Failed to create waypoint');
    return res.json();
  },

  async deleteWaypoint(id, token) {
    const res = await fetch(`/api/waypoints/${id}`, {
      method: 'DELETE',
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!res.ok) throw new Error('Failed to delete waypoint');
    return res.json();
  }
};
