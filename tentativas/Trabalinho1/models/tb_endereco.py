from sqlalchemy import DATETIME, VARCHAR, ForeignKey, CHAR, SMALLINT
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.orm import Mapped, mapped_column
from services.conect_bd import Session, Base
from datetime import datetime
from tb_pessoa import Pessoa, listar_pessoa

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
            f"\nID Endereço: {endereco.id_endereco} | Data de Registro: {endereco.data_criacao} | CEP: {endereco.cep} | "
            f"Logradouro: {endereco.logradouro} | Numero: {endereco.numero} | Bairro: {endereco.bairro} | "
            f"Cidade: {endereco.cidade} | Estado: {endereco.estado} | Nome: {pessoa.nome}"
        )
#=====================================================================================================================================
# listar endereções de uma pessoa.

def listar_endereco_pessoa(session, pessoa_id):
    enderecos = session.query(Endereco).filter_by(id_pessoa=pessoa_id).all()
    
    for endereco in enderecos:
        print(
            f"\nID Endereço: {endereco.id_endereco} | CEP: {endereco.cep} | Logradouro: {endereco.logradouro} | "
            f"Numero: {endereco.numero} | Bairro: {endereco.bairro} | Cidade: {endereco.cidade} | Estado: {endereco.estado}"
        )


#=====================================================================================================================================
# editar endereço

def editar_endereco(session):
    print()
    listar_pessoa(session)
    print()
    pessoa_id = int(input("Digite o ID da pessoa cujo endereço deseja editar: "))

    pessoa = session.query(Pessoa).filter_by(id_pessoa=pessoa_id).first()
    if pessoa:
        listar_endereco_pessoa(session, pessoa_id)
        endereco_id = int(input("Digite o ID do endereço que deseja editar: "))

        endereco = session.query(Endereco).filter_by(id_endereco=endereco_id, id_pessoa=pessoa_id).first()
        if endereco:
            # Solicita as novas informações do endereço
            cep = input("Novo CEP: ")
            logradouro = input("Novo Logradouro: ")
            numero = int(input("Novo Número: "))
            bairro = input("Novo Bairro: ")
            cidade = input("Nova Cidade: ")
            estado = input("Novo Estado: ")

            # Atualiza as informações do endereço
            endereco.cep = cep
            endereco.logradouro = logradouro
            endereco.numero = numero
            endereco.bairro = bairro
            endereco.cidade = cidade
            endereco.estado = estado
            session.commit()
            print("Informações do endereço atualizadas com sucesso.")
        else:
            print(f"Endereço com ID {endereco_id} não encontrado para a pessoa com ID {pessoa_id}.")
    else:
        print(f"Pessoa com ID {pessoa_id} não encontrada.")



#=====================================================================================================================================
# Adicionar endereço a uma pessoa.

def adicionar_endereco(session):
    print()
    listar_pessoa(session)
    print()
    # Solicita os dados do novo endereço
    id_pessoa = int(input("Digite o ID da pessoa a qual deseja adicionar o endereço: "))
    cep = input("CEP: ")
    logradouro = input("Logradouro: ")
    numero = int(input("Número: "))
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")

    # Verifica se a pessoa com o ID fornecido existe
    pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
    if pessoa:
        # Cria um novo registro de endereço
        endereco = Endereco(
            cep=cep,
            logradouro=logradouro,
            numero=numero,
            bairro=bairro,
            cidade=cidade,
            estado=estado,
            id_pessoa=id_pessoa
        )
        session.add(endereco)
        session.commit()
        print("Endereço adicionado com sucesso.")
    else:
        print(f"Pessoa com ID {id_pessoa} não encontrada.")

#=====================================================================================================================================
# exluir endereço


def excluir_endereco(session):
    print()
    listar_pessoa(session)
    print()
    pessoa_id = int(input("\nDigite o ID da pessoa cujo endereço deseja excluir: "))

    pessoa = session.query(Pessoa).filter_by(id_pessoa=pessoa_id).first()
    if pessoa:
        listar_endereco_pessoa(session, pessoa_id)
        endereco_id = int(input("\nDigite o ID do endereço que deseja excluir: "))

        endereco = session.query(Endereco).filter_by(id_endereco=endereco_id, id_pessoa=pessoa_id).first()
        if endereco:
            session.delete(endereco)
            session.commit()
            print("Endereço excluído com sucesso.")
        else:
            print(f"Endereço com ID {endereco_id} não encontrado para a pessoa com ID {pessoa_id}.")
    else:
        print(f"Pessoa com ID {pessoa_id} não encontrada.")

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
            adicionar_endereco(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            editar_endereco(session)
        elif escolha == "4":
            print()
            print(50 * "=")
            print()
            excluir_endereco(session)
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

