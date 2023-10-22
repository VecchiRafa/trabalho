from sqlalchemy import DATETIME, DATE, VARCHAR, CHAR, Enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from services.conect_bd import Session, Base
from datetime import datetime, date

#==========================================================================================================================================================================
# tabela pessoas

class Pessoa(Base):
    __tablename__ = "pessoa"
    
    id_pessoa: Mapped[int] = mapped_column("id_pessoa", INTEGER,nullable=False, autoincrement=True, primary_key=True)
    nome: Mapped[str] =  mapped_column(VARCHAR(100), nullable=False)
    nascimento: Mapped[date] = mapped_column(DATE, nullable=False)
    cpf: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True)
    rg: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True)
    sexo: Mapped[Enum('M','F','NI')] = mapped_column(CHAR(2), nullable=False)
    email: Mapped[str] = mapped_column(VARCHAR(50), nullable=False, unique=True)
    est_civil: Mapped[Enum('SOLTEIRO','CASADO','DIVORCIADO','SEPARADO','VIUVO')] = mapped_column(Enum('SOLTEIRO','CASADO','DIVORCIADO','SEPARADO','VIUVO'), nullable=False)
    nacionalidade: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, default='Brasil')
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())


#==========================================================================================================================================================================
# listar pessoa.

def listar_endereco(session):
    # Consultar endereços e pessoas com informações combinadas
    pessoas = (
        session.query(Pessoa)
        .all()
    )

    for pessoa in pessoas:
        print(
            f" ID: {pessoas.id_pessoa} | Nome: {pessoas.nome} | Nacimento: {pessoas.nascimento} | CPF: {pessoas.cpf} | RG: {pessoas.rg}"
            f" "
        )

#==========================================================================================================================================================================
