# Apache Superset + Postgres (Docker Compose)

This setup runs:
- Apache Superset on `http://localhost:8088`
- Postgres (internal Docker network only)
- Adminer SQL UI on `http://localhost:8080`

Images are intentionally configured to latest tags:
- `apache/superset:latest`
- `postgres:latest`
- `adminer:latest`

## Prerequisites

- Docker Desktop (or Docker Engine + Compose plugin)
- `docker compose` command available

## 1) Configure environment

Copy the environment template:

```bash
cp .env.example .env
```

Generate a strong Superset secret key and place it in `.env`:

```bash
python3 -c "import secrets; print(secrets.token_urlsafe(64))"
```

Update `.env` values as needed (especially passwords and secret key).

## 2) Start the stack

```bash
docker compose up -d
```

## 3) Verify services

Check effective config:

```bash
docker compose config
```

Check service status:

```bash
docker compose ps
```

Check logs if needed:

```bash
docker compose logs -f db superset-init superset sql-client
```

Expected:
- `db` becomes healthy
- `superset-init` exits successfully (code 0) after migrations/init
- `superset` keeps running and serves UI
- `sql-client` keeps running

## 4) Access applications

- Superset: `http://localhost:8088`
  - Login with `SUPERSET_ADMIN_USERNAME` and `SUPERSET_ADMIN_PASSWORD` from `.env`
- Adminer: `http://localhost:8080`
  - System: `PostgreSQL`
  - Server: `db`
  - Username: `POSTGRES_USER`
  - Password: `POSTGRES_PASSWORD`
  - Database: `POSTGRES_DB`

Run SQL smoke test in Adminer:

```sql
SELECT 1;
```

## Common operations

Restart services:

```bash
docker compose restart
```

Stop services:

```bash
docker compose down
```

Full reset (removes containers + volumes/data):

```bash
docker compose down -v
```

If you previously started with a different Postgres data layout, run the reset once before bringing services up again.

## Port conflicts

If ports are already in use, change host bindings in `docker-compose.yml`:
- `127.0.0.1:8088:8088` (Superset)
- `127.0.0.1:8080:8080` (Adminer)

Example: `127.0.0.1:9088:8088` to use `http://localhost:9088`.

## Note on latest tags

Using `latest` is convenient for quick setup but can introduce breaking changes over time. For stable/reproducible environments, pin exact image versions.
