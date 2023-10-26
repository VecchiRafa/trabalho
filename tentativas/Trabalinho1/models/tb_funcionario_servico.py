from services.conect_bd import Base, Session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from tb_servico import Servico
from tb_funcionario import Funcionario

class Funcionario_servico(Base):
    __tablename__ = "funcionario_servico"

    id_funcionario: Mapped[int] = mapped_column("id_funcionario", INTEGER, ForeignKey(Funcionario.id_funcionario), primary_key=True, nullable=False) 
    id_servico: Mapped[int] = mapped_column("id_servico", INTEGER, ForeignKey(Servico.id_servico), primary_key=True, nullable=False) 