from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext

from ..config.settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


secret_key = settings.SECRECT_KEY
algorithm = settings.ALGORITHM

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return bcrypt_context.hash(password)


# def verify_password(plain_password: str, hashed_password: str):
#     print(plain_password, hashed_password)
#     return bcrypt_context.verify(plain_password, hashed_password)
#


def generate_token(
    user_email: str,
    user_id: str,
    expires_delta: timedelta | None = None,
) -> str:
    encode = {"email_user": user_email, "user_id": user_id}

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    encode["exp"] = expire

    return jwt.encode(encode, secret_key, algorithm)


# def check_payload(self, token):
#     decoded_token = jwt.decode(token, self.secret_key, self.algorithm)
#     return decoded_token


# def _validate_token(self, token) -> str:
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#
#     try:
#         return self.check_payload(token)
#     except InvalidTokenError:
#         raise credentials_exception
#


# async def get_token(self, token: Annotated[str | None, Depends(oauth2_scheme)]):
#     self._validate_token(token)
