from sqlalchemy import create_engine, Column, Integer, String, Float, Text, Date, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Configuração da conexão com o banco de dados usando SQLAlchemy
engine = create_engine('mysql://root:Brother25525&@localhost/aunimal_hotel_teste')
Session = sessionmaker(bind=engine)

# Crie uma instância da classe Base
Base = declarative_base()

class Servico(Base):
    __tablename__ = "servico"
    
    id_servico = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(200), nullable=False)
    preco = Column(Float, nullable=False)
    duracao_estimada = Column(Integer, nullable=False)
    descricao = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())

def listar_servicos(session):
    # Consultar serviços
    servicos = session.query(Servico).all()
    for servico in servicos:
        print(f"ID: {servico.id_servico}, Nome: {servico.nome}, Preço: {servico.preco}, Duração Estimada: {servico.duracao_estimada}, Descrição: {servico.descricao}")

def adicionar_servico(session):
    # Coletar informações do usuário
    nome = input("Digite o nome do serviço: ")
    preco = float(input("Digite o preço do serviço: "))
    duracao_estimada = int(input("Digite a duração estimada do serviço (em minutos): "))
    descricao = input("Digite a descrição do serviço (opcional): ")
    
    # Criar uma nova instância de Servico
    novo_servico = Servico(nome=nome, preco=preco, duracao_estimada=duracao_estimada, descricao=descricao)
    
    # Adicionar o serviço à sessão
    session.add(novo_servico)
    
    # Commit para salvar no banco de dados
    session.commit()
    print("Serviço adicionado com sucesso!")

# Iniciar uma sessão
session = Session()

while True:
    print("\nOpções:")
    print("1. Listar serviços")
    print("2. Adicionar serviço")
    print("3. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        listar_servicos(session)
    elif escolha == "2":
        adicionar_servico(session)
    elif escolha == "3":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")

# Fechar a sessão quando terminar
session.close()
