from models import Base, Cliente
from sqlalchemy import INT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INT, TINYINT

class Contato(Base):
    __tablename__ = "contato"

    codigo_pais: Mapped[int] = mapped_column(TINYINT(3, unsigned=True, zerofill=True), nullable=False)
    codigo_area: Mapped[int] = mapped_column(TINYINT(unsigned=True), nullable=False)
    numero: Mapped[int] = mapped_column(INT(unsigned=True), nullable=False)
    id_cliente: Mapped[int] = mapped_column("id_cliente", INT, ForeignKey(Cliente.id_cliente), nullable=False)