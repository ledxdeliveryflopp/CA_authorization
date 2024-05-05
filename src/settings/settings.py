from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    """Настройки для базы данных"""
    user: str
    password: str
    host: str
    port: str
    database_name: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def full_database_ulr(self) -> str:
        """Создание полного URL для БД"""
        return (f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/"
                f"{self.database_name}")


class VaultSettings(BaseSettings):
    """Настройки для HCP Vault"""
    url: str
    token: str
    mount: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class Settings(BaseSettings):
    """Набор всех настроек"""
    database_settings: DatabaseSettings
    vault_settings: VaultSettings


@lru_cache()
def init_settings() -> Settings:
    """Инициализация и кэширование настроек"""
    return Settings(database_settings=DatabaseSettings(), vault_settings=VaultSettings())


settings = init_settings()
