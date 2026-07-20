# AuthRouter

| Eigenschaft | Wert |
|:---|:---|
| **Name** | AuthRouter |
| **Container** | Backend (FastAPI) |
| **Sprache** | Python |

## Aufgabe
FastAPI Router, der die Admin-Authentifizierung verwaltet:

| Methode | Endpunkt | Beschreibung |
|:---|:---|:---|
| `POST` | `/api/auth/login` | Prüft das übermittelte Passwort gegen den `.env`-Wert. Gibt bei Erfolg einen JWT-Token oder Session-Cookie zurück. |

### Sicherheitsmaßnahmen
- **Passwort-Vergleich:** Das Admin-Passwort wird aus der `.env`-Datei gelesen (niemals hartcodiert).
- **Rate Limiting:** Maximal N Versuche pro Zeitintervall, um Brute-Force-Angriffe zu verhindern (AC-1).
- **HTTPS:** Passwort wird nur über verschlüsselte Verbindung übertragen, um Abhören zu verhindern (AC-2).
- **Dependency Injection:** Stellt eine `get_current_admin`-Dependency bereit, die von geschützten Endpunkten (POST/DELETE in [WaypointRouter](waypoint_router.md), [ImageRouter](image_router.md)) verwendet wird.

## Begründung
Die Authentifizierung **muss** serverseitig erfolgen. Ein clientseitiger Passwort-Check wäre trivial zu umgehen (DevTools → JavaScript-Quelle lesen). Das Backend ist die einzige Instanz, die das echte Passwort kennt und den Zugriff gewähren kann.

**User Story Bezug:** UC-4 (Admin-Login)
**Abuse Case Bezug:** AC-1 (Brute Force), AC-2 (Netzwerkpakete)

## Abhängigkeiten
- **Intern:**
  - Wird aufgerufen von → [AdminLogin](../frontend/admin_login.md) (Frontend)
  - Dependency wird genutzt von → [WaypointRouter](waypoint_router.md)
  - Dependency wird genutzt von → [ImageRouter](image_router.md)
- **Extern:** `.env`-Datei mit `ADMIN_PASSWORD`
