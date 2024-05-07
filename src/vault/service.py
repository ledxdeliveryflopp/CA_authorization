from dataclasses import dataclass
from hvac import exceptions, Client
from src.settings.exception import VaultSealed, VaultInvalidPath, VaultInvalidToken
from src.settings.settings import settings


@dataclass
class VaultService:
    """Сервис для HCP Vault"""
    client = Client(url=settings.vault_settings.url, token=settings.vault_settings.token)

    async def create_secret(self, user_id: int, password: str):
        """Сохранение секрета в vault"""
        try:
            self.client.secrets.kv.v2.create_or_update_secret(
                mount_point=settings.vault_settings.mount,
                path=f'{user_id}-password',
                secret=dict(password=f"{password}"))
        except exceptions.VaultDown:
            raise VaultSealed
        except exceptions.Forbidden:
            raise VaultInvalidToken

    async def read_secret(self, user_id: int) -> str:
        """Чтение секрета из vault"""
        try:
            secret_by_vault = self.client.secrets.kv.read_secret_version(
                mount_point=settings.vault_settings.mount, path=f'{user_id}-password')
            secret = secret_by_vault["data"]["data"]["password"]
            return secret
        except exceptions.InvalidPath:
            raise VaultInvalidPath
        except exceptions.Forbidden:
            raise VaultInvalidToken


async def get_vault_service() -> object:
    """Инициализация сервиса Vault"""
    vault_service = VaultService()
    return vault_service
