from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class dogs(Base):
    __tablename__ = "dogs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    gender: Mapped[str] = mapped_column(String(10))
    power: Mapped[int] = mapped_column()
    won_battles: Mapped[int] = mapped_column()
    health: Mapped[int] = mapped_column()