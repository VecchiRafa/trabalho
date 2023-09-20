from models import Base, Funcionario
from sqlalchemy import DATETIME,INT, ForeignKey, DECIMAL, DATE
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INT
from datetime import datetime, date

class Pagamento(Base):
    __tablename__ = "pagamento"
    
    valor: Mapped[int] = mapped_column(DECIMAL(10,2), nullable=False)
    data_pagamento: Mapped[DATETIME] = mapped_column(datetime, nullable=False)
    mes_referencia: Mapped[DATE] = mapped_column(date, nullable=False)
    id_funcionario: Mapped[int] = mapped_column("id_funcionario", INT, ForeignKey(Funcionario.id_funcionario), nullable=False)