from fastapi import APIRouter, Depends, Query, status
from pydantic import BaseModel
from sqlmodel.ext.asyncio.session import AsyncSession

from ..config.database import get_session
from ..services.user_services import UserService

# router = APIRouter(prefix="/api/user", tags=["User"])


class UserDTO(BaseModel):
    email: str
    password: str
    username: str
    is_active: bool = True
    role: str = "client"
    points: float


user_router = APIRouter(prefix="/api/user", tags=["User"])
user_service = UserService()


@user_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    data: UserDTO,
    session: AsyncSession = Depends(get_session),
):
    user = await user_service.create_user(data, session)
    return user
