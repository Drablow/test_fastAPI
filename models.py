from sqlalchemy.orm import Mapped, mapped_column

from database import Model


class TaskOrm(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]


class UserOrm(Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False)
    tg_id: Mapped[int] = mapped_column(unique=True, nullable=False)


