from typing import Any
from fastapi import HTTPException, status


class DetailedHTTPException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Server error"

    def __init__(self, **kwargs: dict[str, Any]) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail, **kwargs)


class UserDontExist(DetailedHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "User don't exist."


class UserExist(DetailedHTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "User already exits."


class VaultSealed(DetailedHTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Vault sealed, contact with api support."


class VaultInvalidPath(DetailedHTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Invalid Vault save path, contact with api support."


class VaultInvalidToken(DetailedHTTPException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Invalid Vault token, contact with api support."
