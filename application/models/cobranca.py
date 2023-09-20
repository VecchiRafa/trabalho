from models import Base, Funcionario, Reserva
from sqlalchemy import INT, DECIMAL, ForeignKey, DATETIME
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INT, FLOAT
from datetime import datetime

class Cobranca(Base):
    __tablename__ = "cobranca"

    id_cobranca: Mapped[int] = mapped_column("id_cobranca", INT,nullable=False, primary_key=True, autoincrement=True)
    data_cobranca: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    valor_total: Mapped[float] = mapped_column(DECIMAL(10,2, unsigned=True), nullable=False)
    id_reserva: Mapped[int] = mapped_column("id_reserva", INT, ForeignKey(Reserva.id_reserva), nullable=False)
    id_funcionario: Mapped[int] = mapped_column("id_funcionario", INT, ForeignKey(Funcionario.id_funcionario), nullable=False)
