from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    name: str
    description: str | None = None


class STask(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class STaskId(BaseModel):
    ok: bool = True
    task_id: int


# схема для создания пользователя (входные данные).
class SUserCreate(BaseModel):
    name: str
    tg_id: int


# расширяет SUserCreate, добавляя id (выходные данные)
class SUser(SUserCreate):
    id: int


# возвращает id созданного пользователя.
class SUserId(BaseModel):
    ok: bool = True
    user_id: int

