from models import Base, Raca
from sqlalchemy import INT, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INT

class Especie(Base):
    __tablename__ = "especie"

    id_especie: Mapped[int] = mapped_column("id_especie", INT,nullable=False, primary_key=True, autoincrement=True)
    tipo: Mapped[Enum('GATO','CACHORRO')] = mapped_column(Enum('GATO','CACHORRO'), nullable=False)
    id_raca: Mapped[int]("id_raca", INT,ForeignKey(Raca.id_raca), autoincrement=True, nullable=False)