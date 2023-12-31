from sqlalchemy import create_engine, ForeignKey, DATETIME
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime
from tb_pessoa import Pessoa
from sqlalchemy import and_
# conexão com a BD(Banco de dados) abaixo
from services.conect_bd import Session, Base

class Cliente(Base):
    __tablename__ = "cliente"
    
    id_cliente: Mapped[int] = mapped_column("id_cliente", INTEGER, ForeignKey(Pessoa.id_pessoa), nullable=False, autoincrement=True, primary_key=True)
    id_pessoa: Mapped[int] = mapped_column("id_pessoa", INTEGER, ForeignKey(Pessoa.id_pessoa), nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    
def adicionar_cliente(session):
    nome = input("Digite o nome da pessoa: ")
    nascimento = input("Digite a data de nascimento (AAAA-MM-DD): ")
    cpf = input("Digite o CPF: ")
    rg = input("Digite o RG: ")
    sexo = input("Digite o sexo (M/F/NI): ")
    email = input("Digite o email: ")
    estado_civil = input("Digite o estado civil (SOLTEIRO, CASADO, DIVORCIADO, SEPARADO, VIUVO): ")
    nacionalidade = input("Digite a nacionalidade: ")
    data_criacao = datetime.now()
    
    # Criar uma nova instância de Pessoa
    nova_pessoa = Pessoa(nome=nome, nascimento=nascimento, cpf=cpf, rg=rg, sexo=sexo, email=email, est_civil=estado_civil,
                         nacionalidade=nacionalidade, data_criacao=data_criacao)
    
    try:
        # Adicionar a pessoa à sessão e fazer o commit para obter o ID gerado
        session.add(nova_pessoa)
        session.commit()

        # Obter o ID_pessoa recém-gerado
        id_pessoa = nova_pessoa.id_pessoa

        # Criar uma nova instância de Cliente associando à nova pessoa
        novo_cliente = Cliente(id_pessoa=id_pessoa)
        session.add(novo_cliente)
        session.commit()
        print( 50 * "\n=")
        print("\n\nCliente adicionado com sucesso!")
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao adicionar o cliente: {e}")



def listar_clientes(session):
    print()

    # Consultar clientes e pessoas com informações combinadas
    clientes_pessoas = session.query(Cliente, Pessoa).filter(Cliente.id_pessoa == Pessoa.id_pessoa).all()
    print(5*"\n\n\n")
    print(50*"=")
    print()
    for cliente, pessoa in clientes_pessoas:
        print(f"ID Cliente: {cliente.id_cliente} | Nome: {pessoa.nome} | CPF: {pessoa.cpf}, "
              f"Nascimento: {pessoa.nascimento} | Sexo: {pessoa.sexo} | Email: {pessoa.email} | estado civil: {pessoa.est_civil} ")


        
def deletar_cliente(session):
    listar_clientes(session)
    print()

    cliente_id = input("Digite o ID do cliente que deseja excluir: ")

    try:
        # Buscar o cliente pelo ID
        cliente = session.query(Cliente).filter(Cliente.id_cliente == cliente_id).one()

        # Remover o cliente
        session.delete(cliente)
        session.commit()
        print("Cliente excluído com sucesso!")
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao excluir o cliente: {e}")

def editar_cliente(session):
    listar_clientes(session)
    print()
    cliente_id = input("Digite o ID do cliente que deseja editar: ")

    try:
        # Buscar o cliente pelo ID
        cliente = session.query(Cliente).filter(Cliente.id_cliente == cliente_id).one()

        # Exibir as informações atuais da pessoa
        dadosPessoais = cliente.pessoa
        print(f"Informações atuais da pessoa:")
        print(f"Nome: {dadosPessoais.nome}")
        print(f"Nascimento: {dadosPessoais.nascimento}")
        print(f"CPF: {dadosPessoais.cpf}")
        print(f"RG: {dadosPessoais.rg}")
        print(f"Sexo: {dadosPessoais.sexo}")
        print(f"Email: {dadosPessoais.email}")
        print(f"Estado Civil: {dadosPessoais.est_civil}")
        print(f"Nacionalidade: {dadosPessoais.nacionalidade}")

        # Coletar as novas informações da pessoa
        nome = input("Digite o novo nome da pessoa: ")
        nascimento = input("Digite a nova data de nascimento (AAAA-MM-DD): ")
        cpf = input("Digite o novo CPF: ")
        rg = input("Digite o novo RG: ")
        sexo = input("Digite o novo sexo (M/F/NI): ")
        email = input("Digite o novo email: ")
        est_civil = input("Digite o estado civil (SOLTEIRO, CASADO, DIVORCIADO, SEPARADO, VIUVO): ")
        nacionalidade = input("Digite a nova nacionalidade: ")

        # Atualizar as informações da pessoa
        dadosPessoais.nome = nome
        dadosPessoais.nascimento = nascimento
        dadosPessoais.cpf = cpf
        dadosPessoais.rg = rg
        dadosPessoais.sexo = sexo
        dadosPessoais.email = email
        dadosPessoais.est_civil = est_civil
        dadosPessoais.nacionalidade = nacionalidade

        session.commit()
        print("Cliente atualizado com sucesso!")
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao editar o cliente: {e}")

def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar clientes")
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
            editar_cliente(session)
        elif escolha == "4":
            print()
            print(50 * "=")
            print()
            deletar_cliente(session)
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
