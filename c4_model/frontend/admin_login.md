# AdminLogin

| Eigenschaft | Wert |
|:---|:---|
| **Name** | AdminLogin |
| **Container** | Frontend (Vue.js) |
| **Sprache** | JavaScript / Vue.js SFC |

## Aufgabe
Rendert eine Login-Maske unter der versteckten Vue-Router-Route `/wal`. Der Admin gibt dort sein Passwort ein. Das Passwort wird via [ApiClient](api_client.md) an das Backend gesendet, welches es gegen das in der `.env` hinterlegte Passwort prüft. Bei Erfolg wird ein Token (oder Session-Cookie) zurückgegeben und der Admin wird zum [AdminPanel](admin_panel.md) weitergeleitet.

## Begründung
Die Passwort-Validierung **muss** serverseitig stattfinden, um Manipulation über die DevTools zu verhindern (Abuse Case AC-2). Die versteckte Route `/wal` stellt sicher, dass normale Besucher den Admin-Bereich nicht zufällig finden.

**User Story Bezug:** UC-4 (Admin über `/wal` erreichen)
**Abuse Case Bezug:** AC-1 (Brute Force), AC-2 (Netzwerkpakete auslesen)

## Abhängigkeiten
- **Intern:**
  - Sendet Passwort an das Backend über → [ApiClient](api_client.md)
  - Backend-Validierung erfolgt in → [AuthRouter](../backend/auth_router.md)
  - Leitet bei Erfolg weiter zu → [AdminPanel](admin_panel.md)
