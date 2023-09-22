from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Configuração da conexão com o banco de dados usando SQLAlchemy
engine = create_engine('mysql://root:Brother25525&@localhost/aunimalhotel')
Session = sessionmaker(bind=engine)

# Crie uma instância da classe Base
Base = declarative_base()

class Associado(Base):
    __tablename__ = "associado"
    
    id_associado = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    nascimento = Column(Date, nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    rg = Column(String(11), nullable=False, unique=True)
    sexo = Column(String(2), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    nacionalidade = Column(String(100), nullable=False, default='Brasil')
    data_criacao = Column(DateTime, nullable=False)

class Cliente(Base):
    __tablename__ = "cliente"
    
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    id_associado = Column(Integer, ForeignKey('associado.id_associado'), nullable=False)
    
    # Adicione um relacionamento para acessar os dados do associado
    associado = relationship('Associado', backref='cliente')

    def __init__(self, id_associado):
        self.id_associado = id_associado

def listar_clientes(session):  
    # Consultar clientes e associados com informações combinadas
    clientes_associados = session.query(Cliente, Associado).join(Associado).all()
    
    for cliente, associado in clientes_associados:
        print(f"ID Cliente: {cliente.id_cliente}, Nome: {associado.nome}, CPF: {associado.cpf}, "
              f"Nascimento: {associado.nascimento}, Sexo: {associado.sexo}, Email: {associado.email}")

def adicionar_cliente(session):
    # Coletar informações do associado
    nome = input("Digite o nome do associado: ")
    nascimento = input("Digite a data de nascimento (AAAA-MM-DD): ")
    cpf = input("Digite o CPF: ")
    rg = input("Digite o RG: ")
    sexo = input("Digite o sexo (M/F/NI): ")
    email = input("Digite o email: ")
    nacionalidade = input("Digite a nacionalidade: ")
    data_criacao = datetime.now()
    
    # Criar uma nova instância de Associado
    novo_associado = Associado(nome=nome, nascimento=nascimento, cpf=cpf, rg=rg, sexo=sexo, email=email,
                               nacionalidade=nacionalidade, data_criacao=data_criacao)
    
    try:
        # Adicionar o associado à sessão e fazer o commit para obter o ID gerado
        session.add(novo_associado)
        session.commit()

        # Obter o ID_associado recém-gerado
        id_associado = novo_associado.id_associado

        # Criar uma nova instância de Cliente associando ao novo associado
        novo_cliente = Cliente(id_associado=id_associado)
        session.add(novo_cliente)
        session.commit()
        
        print("Cliente adicionado com sucesso!")
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao adicionar o cliente: {e}")

def deletar_cliente(session):
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
    cliente_id = input("Digite o ID do cliente que deseja editar: ")

    try:
        # Buscar o cliente pelo ID
        cliente = session.query(Cliente).filter(Cliente.id_cliente == cliente_id).one()

        # Exibir as informações atuais do associado
        associado = cliente.associado
        print(f"Informações atuais do associado:")
        print(f"Nome: {associado.nome}")
        print(f"Nascimento: {associado.nascimento}")
        print(f"CPF: {associado.cpf}")
        print(f"RG: {associado.rg}")
        print(f"Sexo: {associado.sexo}")
        print(f"Email: {associado.email}")
        print(f"Nacionalidade: {associado.nacionalidade}")

        # Coletar as novas informações do associado
        nome = input("Digite o novo nome do associado: ")
        nascimento = input("Digite a nova data de nascimento (AAAA-MM-DD): ")
        cpf = input("Digite o novo CPF: ")
        rg = input("Digite o novo RG: ")
        sexo = input("Digite o novo sexo (M/F/NI): ")
        email = input("Digite o novo email: ")
        nacionalidade = input("Digite a nova nacionalidade: ")

        # Atualizar as informações do associado
        associado.nome = nome
        associado.nascimento = nascimento
        associado.cpf = cpf
        associado.rg = rg
        associado.sexo = sexo
        associado.email = email
        associado.nacionalidade = nacionalidade

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
