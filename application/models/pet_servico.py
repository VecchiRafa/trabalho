from models import Base, Pet, Servico
from sqlalchemy import INT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INT


class Pet_servico(Base):
    __tablename__ = "pet_servico"

    id_pet: Mapped[int] = mapped_column("id_pet", INT, ForeignKey(Pet.id_pet), primary_key=True, nullable=False) 
    id_servico: Mapped[int] = mapped_column("id_servico", INT, ForeignKey(Servico.id_servico), primary_key=True, nullable=False) 