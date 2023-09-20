from models import Base
from sqlalchemy import INT, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INT


class Raca(Base):
    __tablename__ = "raca"

    id_raca: Mapped[int] = mapped_column("id_raca", INT,nullable=False, primary_key=True, autoincrement=True)
    classificacao: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
