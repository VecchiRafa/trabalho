from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Configuração da conexão com o banco de dados usando SQLAlchemy
engine = create_engine('mysql://root:Brother25525&@localhost/aunimalhotel')
Session = sessionmaker(bind=engine)

# Crie uma instância da classe Base
Base = declarative_base()

class TbEspecie(Base):
    __tablename__ = "especie"

    id_especie = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(25), nullable=False)

def listar_especie(session,):
    #consultar especies
    especies = session.query(TbEspecie).all()
    for especie in especies:
        print(f" ID especie: {especie.id_especie}, Tipo: {especie.tipo}")

class TbRaca(Base):
    __tablename__ = "raca"

    id_raca = Column(Integer, primary_key=True, autoincrement=True)
    classificacao = Column(String(100), nullable=True)
    id_especie = Column(Integer, nullable=True)

def listar_raca(session, id_especie):
    #consultar raça
    racas = session.query(TbRaca).filter_by(id_especie=id_especie).all()
    for raca in racas:
        print(f"ID raça: {raca.id_raca}, classificação: {raca.classificacao}, ID especie: {raca.id_especie} ")

def adicionar_raca(session):
    # Coletar informações da raça
    
    classificacao = input("Digite a classificação: ")
    print()
    listar_especie(session)
    print()
    existe = input("A especie desejada existe(S/N): ").strip().lower()

    if existe == "s":
        id_especie = input("Disgite o ID da especie desejada: ")

    else:
        #adiciona uma nova especie 
        tipo = input("Digite o tipo da especie: ")

        nova_especie = TbEspecie(tipo=tipo)

        session.add(nova_especie)

        session.commit()
        print("Raça adicionada com sucesso!")
        print()
        listar_especie(session)
        print()
        id_especie = input("Disgite o ID da especie desejada: ")
    
    
    
    # Criar uma nova instância de TbPet
    nova_raca = TbRaca(classificacao=classificacao, id_especie=id_especie)
    
    # Adicionar o pet à sessão
    session.add(nova_raca)
    
    # Commit para salvar no banco de dados
    session.commit()
    print("Raça adicionada com sucesso!")
    print()

def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print("\nOpções:")
        print("1. Listar raça")
        print("2. Adicionar raça")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            print(50*"=")
            print()
            listar_especie(session)
            print()
            id_especie = input("digite o ID da especie desejada: ")
            print()
            listar_raca(session, id_especie)
        elif escolha == "2":
            print()
            adicionar_raca(session)
        elif escolha == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Fechar a sessão quando terminar
    session.close()

if __name__ == "__main__":
    executar()
