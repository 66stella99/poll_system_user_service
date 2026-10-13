# Poll System — User Service

Saves the poll system users. Works together with the
[Poll Service](https://github.com/66stella99/poll_system_poll_service).

Stack: Python, FastAPI, MySQL, Docker & Docker Compose.
Structure: `controller` → `service` → `repository`, with `model`, `config` and `api` (calls to the poll service).

## Run

```bash
docker compose up -d --build
```

Swagger UI: http://localhost:8001/docs

## Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/user/` | Get all users |
| GET | `/user/{user_id}` | Get user info |
| POST | `/user/` | Create a user (`is_registered` starts as `false`) |
| PUT | `/user/{user_id}` | Update a user |
| PUT | `/user/{user_id}/register` | Register an existing user (`is_registered` → `true`) |
| DELETE | `/user/{user_id}` | Delete a user — also deletes all of its answers in the poll service |

Create / update body:

```json
{
  "first_name": "Alice",
  "last_name": "Smith",
  "email": "alice@example.com",
  "age": 28,
  "address": "12 Herzl St, Tel Aviv",
  "joining_date": "2023-01-15"
}
```
