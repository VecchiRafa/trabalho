from models import Base, Funcionario, Servico
from sqlalchemy import INT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INT

class Funcionario_servico(Base):
    __tablename__ = "funcionario_servico"

    id_funcionario: Mapped[int] = mapped_column("id_funcionario", INT, ForeignKey(Funcionario.id_funcionario), primary_key=True, nullable=False) 
    id_servico: Mapped[int] = mapped_column("id_servico", INT, ForeignKey(Servico.id_servico), primary_key=True, nullable=False) 