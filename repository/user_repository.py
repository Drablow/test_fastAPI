from sqlalchemy import select
from database import new_session
from models import UserOrm
from schemas import SUserCreate, SUser


class UserRepository:
    @classmethod
    async def add_one(cls, data: SUserCreate)-> int:
        async with new_session() as session:
            user_dict = data.model_dump()
            user = UserOrm(**user_dict)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id

    @classmethod
    async def get_all(cls) -> list[SUser]:
        async with new_session() as session:
            query = select(UserOrm)
            result = await session.execute(query)
            user_models = result.scalars().all()
            return [SUser.model_validate(user_model) for user_model in user_models]

