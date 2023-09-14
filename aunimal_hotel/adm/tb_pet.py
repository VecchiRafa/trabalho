from sqlalchemy import create_engine, Column, Integer, String, Float, CHAR, Date, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, date

# Configuração da conexão com o banco de dados usando SQLAlchemy
engine = create_engine('mysql://root:Brother25525&@localhost/aunimalhotel')
Session = sessionmaker(bind=engine)

# Crie uma instância da classe Base
Base = declarative_base()

class TbPet(Base):
    __tablename__ = "pet"
    
    id_pet = Column(Integer, primary_key=True, autoincrement=True)
    data_criacao = Column(DateTime, nullable=False, default=datetime.now())
    nome = Column(String(200), nullable=False)
    peso = Column(Float, nullable=True)
    sexo = Column(CHAR(2), nullable=True)
    porte = Column(String(50), nullable=True)
    nascimento = Column(Date, nullable=True)
    descricao = Column(String(200), nullable=True)
    id_especie = Column(Integer, nullable=False)
    id_raca = Column(Integer, nullable=False)

class TbEspecie(Base):
    __tablename__ = "especie"

    id_especie = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(25), nullable=False)

class TbRaca(Base):
    __tablename__ = "raca"

    id_raca = Column(Integer, primary_key=True, autoincrement=True)
    classificacao = Column(Integer, nullable=True)
    id_especie = Column(Integer, nullable=True)

def listar_especie(session,):
    #consultar especies
    especies = session.query(TbEspecie).all()
    for especie in especies:
        print(f" ID especie: {especie.id_especie}, Tipo: {especie.tipo}")

def listar_raca(session):
    #consultar raça
    racas = session.query(TbRaca).all()
    for raca in racas:
        print(f"ID raça: {raca.id_raca}, classificação: {raca.classificacao}")

def listar_pet(session):
    # Consultar pets
    pets = session.query(TbPet).all()
    for pet in pets:
        print(f"ID Pet: {pet.id_pet}, Nome: {pet.nome}, Peso: {pet.peso}, Sexo: {pet.sexo}, Porte: {pet.porte}, Nascimento: {pet.nascimento}, Descrição: {pet.descricao}, ID Espécie: {pet.id_especie}, ID Raça: {pet.id_raca}")

def adicionar_pet(session):
    # Coletar informações do pet
    nome = input("Digite o nome do pet: ")
    peso = float(input("Digite o peso do pet: "))
    sexo = input("Digite o sexo do pet (M/F): ")
    porte = input("Digite o porte do pet (PP/P/M/G/GG): ")
    nascimento = input("Digite a data de nascimento do pet (YYYY-MM-DD): ")
    descricao = input("Digite a descrição do pet: ")
    listar_especie(session)
    id_especie = int(input("Digite o ID da espécie do pet: "))
    listar_raca(session)
    id_raca = int(input("Digite o ID da raça do pet: "))
    
    # Converter a data de nascimento para o formato Date
    try:
        nascimento = datetime.strptime(nascimento, "%Y-%m-%d").date()
    except ValueError:
        print("Formato de data inválido. Use o formato YYYY-MM-DD.")
        return
    
    # Criar uma nova instância de TbPet
    novo_pet = TbPet(nome=nome, peso=peso, sexo=sexo, porte=porte, nascimento=nascimento, descricao=descricao, id_especie=id_especie, id_raca=id_raca)
    
    # Adicionar o pet à sessão
    session.add(novo_pet)
    
    # Commit para salvar no banco de dados
    session.commit()
    print("Pet adicionado com sucesso!")

def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print("\nOpções:")
        print("1. Listar pets")
        print("2. Adicionar pet")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            print(50*"=")
            print()
            listar_pet(session)
        elif escolha == "2":
            adicionar_pet(session)
        elif escolha == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Fechar a sessão quando terminar
    session.close()

if __name__ == "__main__":
    executar()
