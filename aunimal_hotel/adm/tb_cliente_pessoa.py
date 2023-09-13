from sqlalchemy import create_engine, Column, Integer, String, CHAR, Date, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, date

# Configuração da conexão com o banco de dados usando SQLAlchemy
engine = create_engine('mysql://root:Brother25525&@localhost/aunimal_hotel')
Session = sessionmaker(bind=engine)

# Crie uma instância da classe Base
Base = declarative_base()

class ClientePessoa(Base):
    __tablename__ = "cliente_pessoa"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    cpf = Column(CHAR(11), nullable=False, unique=True)
    birth_date = Column(Date, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())

def listar_clientes(session):
    # Consultar clientes
    clientes = session.query(ClientePessoa).all()
    for cliente in clientes:
        print(f"ID: {cliente.id}, Nome: {cliente.name}, CPF: {cliente.cpf}")

def adicionar_cliente(session):
    # Coletar informações do usuário
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    data_nascimento = input("Digite a data de nascimento do cliente (YYYY-MM-DD): ")
    
    # Converter a data de nascimento para o formato Date
    try:
        data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
    except ValueError:
        print("Formato de data inválido. Use o formato YYYY-MM-DD.")
        return
    
    # Criar uma nova instância de ClientePessoa
    novo_cliente = ClientePessoa(name=nome, cpf=cpf, birth_date=data_nascimento)
    
    # Adicionar o cliente à sessão
    session.add(novo_cliente)
    
    # Commit para salvar no banco de dados
    session.commit()
    print("Cliente adicionado com sucesso!")

def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print("\nOpções:")
        print("1. Listar tabela")
        print("2. Adicionar cliente")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            print(50*"=")
            print()
            listar_clientes(session)
        elif escolha == "2":
            adicionar_cliente(session)
        elif escolha == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Fechar a sessão quando terminar
    session.close()

if __name__ == "__main__":
    executar()
