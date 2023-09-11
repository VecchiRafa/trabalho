from models import Base
from sqlalchemy import DATETIME, VARCHAR, DATE, CHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT
from datetime import datetime

class Pessoa(Base):
    __tablename__ = "pessoa"
    id: Mapped[int] = mapped_column("id", MEDIUMINT, 
                                            nullable=False,
                                            autoincrement=True,
                                            primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DATETIME, 
                                                    nullable=False,
                                                    default=datetime.now())
    name: Mapped[str] = mapped_column(VARCHAR(200),nullable=False)
    cpf: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True)
    birth_date: Mapped[date] = mapped_column(DATE, nullable=False)
