#-----------------------------------------------------------------------------------------------------------------------------------
#import's das funções e tabelas.

from sqlalchemy import DATETIME, VARCHAR, ForeignKey, CHAR, SMALLINT
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.orm import Mapped, mapped_column
from services.conect_bd import Session, Base
from datetime import datetime
from models.tb_pessoa import Pessoa

#=======================================================================================================================================
# tabela de endereço pertencente a tabela pessoas.

class Endereco(Base):
    __tablename__ = "endereco"

    id_endereco: Mapped[int] = mapped_column("id_endereco", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    cep: Mapped[str] = mapped_column(CHAR(8), nullable=False)
    logradouro: Mapped[str] = mapped_column(VARCHAR(50))
    numero:Mapped[SMALLINT] = mapped_column(SMALLINT, nullable=False)
    bairro: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    cidade: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    estado: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    id_pessoa: Mapped[int] = mapped_column("id_pessoa", INTEGER, ForeignKey(Pessoa.id_pessoa), primary_key=True, nullable=False)

#=====================================================================================================================================
# listar endereco.

def listar_endereco(session):
    # Consultar endereços e pessoas com informações combinadas
    enderecos_pessoas = (
        session.query(Endereco, Pessoa)
        .join(Pessoa, Endereco.id_pessoa == Pessoa.id_pessoa)
        .all()
    )

    for endereco, pessoa in enderecos_pessoas:
        print(
            f"ID Endereço: {endereco.id_endereco} | Data de Registro: {endereco.data_criacao} | CEP: {endereco.cep} | "
            f"Logradouro: {endereco.logradouro} | Numero: {endereco.numero} | Bairro: {endereco.bairro} | "
            f"Cidade: {endereco.cidade} | Estado: {endereco.estado} | Nome: {pessoa.nome}"
        )

#=====================================================================================================================================
# Adicionar endereço a uma pessoa da tabela pessoa.

def adicionar_endereco(session):
    
    endereco_novo = input("digite ")

#=====================================================================================================================================
#=====================================================================================================================================
def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar endereço")
        print("2. Adicionar endereço")
        print("3. Editar endereço")
        print("4. Deletar endereço")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_endereco(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            #adicionar_especie(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
           # editar_especie(session)
        elif escolha == "4":
            print()
            print(50 * "=")
            print()
          #  deletar_especie(session)
        elif escolha == "5":
            print()
            print(50 * "=")
            print()
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Fechar a sessão quando terminar
    session.close()

if __name__ == "__main__":
    executar()

