from models import Base, Cobranca, Forma
from sqlalchemy import INT, DECIMAL, ForeignKey, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INT

class Cobranca_forma(Base):
    __tablename__ = "cobranca_forma"

    valor: Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)
    parcela: Mapped[str] = mapped_column(VARCHAR(45), nullable=True)
    id_cobranca: Mapped[int] = mapped_column("id_cobranca", INT,ForeignKey(Cobranca.id_cobranca), nullable=False)
    id_forma: Mapped[int] = mapped_column("id_forma", INT,ForeignKey(Forma.id_forma), nullable=False)