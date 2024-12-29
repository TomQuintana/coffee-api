from enum import Enum

from sqlmodel import Field, SQLModel


class UserRole(str, Enum):
    ADMIN = "admin"
    CLIENT = "client"


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, nullable=False, unique=True)
    email: str = Field(nullable=False, unique=True)
    hashed_password: str = Field(nullable=False)
    role: UserRole = Field(default=UserRole.CLIENT)
    is_active: bool = Field(default=True)
    points: float = Field(default=0)
