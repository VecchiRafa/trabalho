from models import Base, Cliente, Funcionario
from sqlalchemy import DATETIME,INT, DECIMAL, VARCHAR, FLOAT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INT
from datetime import datetime

class Reserva(Base):
    __tablename__ = "reserva"
    
    id_reserva: Mapped[int] = mapped_column("id_reserva", INT,nullable=False, primary_key=True, autoincrement=True)
    check_in: Mapped[datetime] = mapped_column(DATETIME,nullable=False,default=datetime.now())
    checkout: Mapped[datetime] = mapped_column(DATETIME,nullable=False,default=datetime.now())
    descricao: Mapped[str] = mapped_column(VARCHAR(200),nullable=True)
    valor_total: Mapped[float] = mapped_column(DECIMAL(10,2),nullable=False)
    id_cliente: Mapped[int] = mapped_column("id_cliente",INT, ForeignKey(Cliente.id_cliente), nullable=False)
    id_funcionario: Mapped[int] = mapped_column("id_funcionario", INT, ForeignKey(Funcionario.id_funcionario), nullable=False)