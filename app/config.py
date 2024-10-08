from typing import Any, Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Настройка приложения"""

    MODE: Literal["TEST", "DEV"] = "DEV"

    # данные для базы данных PostgreSQL
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    # данные для тестовой базы данных PostgreSQL
    TEST_DB_HOST: str
    TEST_DB_PORT: int
    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_NAME: str

    # ключ для хешировани пользовательских паролей
    SECRET_KEY: str

    # алгоритм шифрования для JWT токена
    ALGORITHM: str = "HS256"

    COOKIE_KEY: str = "notes_access_token"

    SPELLER_URL: str

    @property
    def DATABASE_URL(self):
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@"
            + f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    @property
    def TEST_DATABASE_URL(self) -> str:
        """URL адрес тестовой базы данных."""
        return (
            f"postgresql+asyncpg://{self.TEST_DB_USER}:{self.TEST_DB_PASS}@"
            f"{self.TEST_DB_HOST}:{self.TEST_DB_PORT}/{self.TEST_DB_NAME}"
        )

    model_config = SettingsConfigDict(env_file=".env")


def get_settings(**kwargs: Any) -> Settings:
    return Settings(**kwargs)
