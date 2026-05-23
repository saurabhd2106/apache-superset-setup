import os


def _required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


SECRET_KEY = _required_env("SUPERSET_SECRET_KEY")

POSTGRES_USER = _required_env("POSTGRES_USER")
POSTGRES_PASSWORD = _required_env("POSTGRES_PASSWORD")
POSTGRES_DB = _required_env("POSTGRES_DB")

SQLALCHEMY_DATABASE_URI = (
    f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}"
)
