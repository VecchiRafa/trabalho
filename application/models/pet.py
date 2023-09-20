from models import Base, Especie, Cliente
from sqlalchemy import DATETIME,INT, DECIMAL, VARCHAR, DATE, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INT, FLOAT
from datetime import datetime, date

class Pet(Base):
    __tablename__ = "pet"

    id_pet: Mapped[int] = mapped_column("id_pet", INT,nullable=False, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    nome: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    peso: Mapped[float] = mapped_column(DECIMAL(5,2), nullable=True)
    sexo: Mapped[Enum('M', 'F')] = mapped_column(Enum('M', 'F'), nullable=False)
    pelagem: Mapped[str] = mapped_column(VARCHAR(100), nullable=True)
    porte: Mapped[Enum('PP', 'P', 'M', 'G', 'GG')] = mapped_column(Enum('PP', 'P', 'M', 'G', 'GG'), nullable=False)
    nascimento: Mapped[date] = mapped_column(DATE, nullable=True)
    descricao: Mapped[str] = mapped_column(VARCHAR(200), nullable=True)
    id_especie: Mapped[int] = mapped_column("id_especie", INT, ForeignKey(Especie.id_especie), primary_key=True, nullable=False) # chave PK Fk coloca junto?
    id_cliente: Mapped[int] = mapped_column("id_cliente", INT, ForeignKey(Cliente.id_cliente), nullable=False)