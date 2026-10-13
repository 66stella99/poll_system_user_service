from pydantic import model_validator
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    MYSQL_USER: str = "user"
    MYSQL_PASSWORD: str = "password"
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3308
    MYSQL_DATABASE: str = "user_service"
    DATABASE_URL: str = ""

    POLL_SERVICE_URL: str = "http://localhost:8002"
    HTTP_TIMEOUT_SECONDS: float = 5.0

    @model_validator(mode="after")
    def build_database_url(self) -> "Config":
        if not self.DATABASE_URL:
            self.DATABASE_URL = (
                f"mysql+aiomysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}"
                f"@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"
            )
        return self


config = Config()
