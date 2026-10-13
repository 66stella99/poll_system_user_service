from pydantic import BaseSettings


class Config(BaseSettings):
    MYSQL_USER: str = "user"
    MYSQL_PASSWORD: str = "password"
    MYSQL_DATABASE: str = "user_service"
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: str = "3308"
    DATABASE_URL: str = f"mysql+aiomysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    POLL_SERVICE_URL: str = "http://localhost:8002"
