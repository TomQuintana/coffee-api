from fastapi import HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from ..models.user.user_model import User
from ..utils.auth_utils import hash_password


class UserService:
    async def get_user_by_email(self, email: str, username: str, session: AsyncSession):
        statement = select(User).where(User.email == email, User.username == username)

        result = await session.exec(statement)

        user = result.first()

        return user

    async def user_exists(self, email, username, session: AsyncSession):
        user = await self.get_user_by_email(email, username, session)

        return True if user is not None else False

    async def create_user(self, user_data: dict, session: AsyncSession):
        user_data_dict = user_data.model_dump()

        is_user_exists = await self.user_exists(
            user_data_dict["email"], user_data_dict["username"], session
        )
        if is_user_exists:
            print("User already exists")
            raise HTTPException(status_code=400, detail="User already exists")

        new_user = User(**user_data_dict)

        new_user.hashed_password = hash_password(user_data_dict["password"])

        session.add(new_user)

        await session.commit()

        return new_user
