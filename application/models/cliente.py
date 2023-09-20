from models import Base, Pessoa 
from sqlalchemy import INT, ForeignKey, DATETIME
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INT
from datetime import datetime

class Cliente(Base):
    __tablename__ = "cliente"
    
    id_cliente: Mapped[int] = mapped_column("id_cliente", INT, ForeignKey(Pessoa.id_pessoa), primary_key=True, nullable=False, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
   