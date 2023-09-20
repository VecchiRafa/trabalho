from models import Base, Reserva, Pet
from sqlalchemy import INT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INT

class Pet_reserva (Base):
    __tablename__ = "pet_reserva"

    id_pet: Mapped[int] = mapped_column("id_pet", INT, ForeignKey(Pet.id_pet), primary_key=True, nullable=False) 
    id_reserva: Mapped[int] = mapped_column("id_reserva", INT, ForeignKey(Reserva.id_reserva), primary_key=True, nullable=False) 
