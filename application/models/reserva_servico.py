from models import Base, Reserva, Servico
from sqlalchemy import INT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INT

class Reserva_servico(Base):
    __tablename__ = "reserva_servico"

    id_reserva: Mapped[int] = mapped_column("id_reserva", INT, ForeignKey(Reserva.id_reserva), primary_key=True, nullable=False) 
    id_servico: Mapped[int] = mapped_column("id_servico", INT, ForeignKey(Servico.id_servico), primary_key=True, nullable=False) 