from services.conect_bd import Base, Session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from tb_reserva import Reserva
from tb_pet import Pet

class Pet_reserva (Base):
    __tablename__ = "pet_reserva"

    id_pet: Mapped[int] = mapped_column("id_pet", INTEGER, ForeignKey(Pet.id_pet), primary_key=True, nullable=False) 
    id_reserva: Mapped[int] = mapped_column("id_reserva", INTEGER, ForeignKey(Reserva.id_reserva), primary_key=True, nullable=False) 