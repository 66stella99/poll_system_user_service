# Poll System — User Service

Backend service that stores the poll system users. Part of the Poll System project together with the
[Poll Service](https://github.com/66stella99/poll_system_poll_service).

**Stack:** Python · FastAPI · MySQL · Docker & Docker Compose

## Responsibilities

- Full CRUD for users (id, first name, last name, email, age, address, joining date, is registered)
- Registering an existing user is a separate step from creating it — new users start with `is_registered = false`
- Only registered users can answer poll questions (the poll service checks this through this service's API)
- Deleting a user also deletes all of its answers, by calling the poll service API

## Architecture

```
controller/  → HTTP endpoints (request → response)
service/     → business logic
repository/  → SQL queries against the service's own MySQL DB
model/       → request / response models (UserRequest → User)
api/         → client for the poll service API
config/      → settings, overridable with environment variables
resources/db-migrations/init.sql → table + seed data
```

## Running

### Everything in Docker

```bash
docker compose up -d --build
```

- API: http://localhost:8001 — Swagger UI: http://localhost:8001/docs
- MySQL: `localhost:3308` (db `user_service`, user `user` / `password`)

### Locally (e.g. from PyCharm)

```bash
docker compose up -d mysql
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

The poll service is expected at `http://localhost:8002` (`POLL_SERVICE_URL`).

## Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/user/` | Get all users |
| GET | `/user/{user_id}` | Get user info |
| POST | `/user/` | Create a user (not registered yet) |
| PUT | `/user/{user_id}` | Update a user |
| PUT | `/user/{user_id}/register` | Register an existing user (`is_registered` → `true`) |
| DELETE | `/user/{user_id}` | Delete a user and all of its poll answers |

Example body for create / update:

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

## Configuration

| Variable | Default |
|---|---|
| `MYSQL_HOST` / `MYSQL_PORT` | `localhost` / `3308` |
| `MYSQL_USER` / `MYSQL_PASSWORD` | `user` / `password` |
| `MYSQL_DATABASE` | `user_service` |
| `POLL_SERVICE_URL` | `http://localhost:8002` |
