from sqlalchemy import DATETIME, VARCHAR, ForeignKey, CHAR, SMALLINT
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT
from sqlalchemy.orm import Mapped, mapped_column
from services.conect_bd import Session, Base
from datetime import datetime
from tb_pessoa import Pessoa, listar_pessoa

class Cliente(Base):
    __tablename__ = "cliente"
    
    id_cliente: Mapped[int] = mapped_column("id_cliente", INTEGER, ForeignKey(Pessoa.id_pessoa), nullable=False, autoincrement=True, primary_key=True)
    id_pessoa: Mapped[int] = mapped_column("id_pessoa", INTEGER, ForeignKey(Pessoa.id_pessoa), nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())


def adicionar_cliente(session):
    nome = input("Nome: ")
    nascimento = input("Data de Nascimento (AAAA-MM-DD): ")
    cpf = input("CPF: ")
    rg = input("RG: ")
    sexo = input("Sexo (M/F/NI): ")
    email = input("Email: ")
    est_civil = input("Estado Civil (SOLTEIRO/CASADO/DIVORCIADO/SEPARADO/VIUVO): ")
    nacionalidade = input("Nacionalidade (Opcional, pressione Enter para usar 'Brasil'): ")

    nova_pessoa = Pessoa(
        nome=nome,
        nascimento=nascimento,
        cpf=cpf,
        rg=rg,
        sexo=sexo,
        email=email,
        est_civil=est_civil,
        nacionalidade=nacionalidade
    )

    session.add(nova_pessoa)
    session.commit()

    # Agora pegue o ID da pessoa recém-criada
    id_pessoa = nova_pessoa.id_pessoa

    novo_cliente = Cliente(id_pessoa=id_pessoa)
    session.add(novo_cliente)
    session.commit()

    print("Cliente adicionado com sucesso.")


# Função para listar todos os clientes
def listar_clientes(session):
    # Consultar clientes e informações da tabela Pessoa combinadas
    clientes_pessoas = session.query(Cliente, Pessoa).filter(Cliente.id_pessoa == Pessoa.id_pessoa).all()
    
    for cliente, pessoa in clientes_pessoas:
        print(f"ID Cliente: {cliente.id_cliente} | ID Pessoa: {cliente.id_pessoa}"
              f"Nome: {pessoa.nome} | "
              f"Nascimento: {pessoa.nascimento} | "
              f"CPF: {pessoa.cpf} | "
              f"RG: {pessoa.rg} | "
              f"Sexo: {pessoa.sexo} | "
              f"Email: {pessoa.email} | "
              f"Estado Civil: {pessoa.est_civil} | "
              f"Nacionalidade: {pessoa.nacionalidade} | "
              f"Data de Criação: {pessoa.data_criacao}"
              )
              


# Função para atualizar informações de um cliente
def atualizar_cliente(cliente_id, novo_id_pessoa, session):
    cliente = session.query(Cliente).filter_by(id_cliente=cliente_id).first()
    if cliente:
        cliente.id_pessoa = novo_id_pessoa
        session.commit()
        print("Informações do cliente atualizadas com sucesso.")
    else:
        print(f"Cliente com ID {cliente_id} não encontrado.")

# Função para excluir um cliente
def excluir_cliente(session):
    listar_clientes(session)
    cliente_id = int(input("Digite o ID do cliente que deseja deletar: "))

    cliente = session.query(Cliente).filter_by(id_cliente=cliente_id).first()
    if cliente:
        pessoa = session.query(Pessoa).filter_by(id_pessoa=cliente.id_pessoa).first()
        if pessoa:
            session.delete(cliente)
            session.delete(pessoa)
            session.commit()
            print("Cliente e Pessoa associada excluídos com sucesso.")
        else:
            print(f"Pessoa associada ao cliente com ID {cliente_id} não encontrada.")
    else:
        print(f"Cliente com ID {cliente_id} não encontrado.")



#=====================================================================================================================================
def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar cliente")
        print("2. Adicionar cliente")
        print("3. Editar cliente")
        print("4. Deletar cliente")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_clientes(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_cliente(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            atualizar_cliente(session)
        elif escolha == "4":
            print()
            print(50 * "=")
            print()
            excluir_cliente(session)
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
