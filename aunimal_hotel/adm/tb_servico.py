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
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    valor_total = Column(Float, nullable=False)
    descricao = Column(Text, nullable=True)
    

def listar_servicos(session):
    # Consultar serviços com as informações desejadas (id, valor_total e descricao)
    servicos = session.query(Servico.id, Servico.valor_total, Servico.descricao).all()
    
    for servico in servicos:
        id, valor_total, descricao = servico
        print(f"id: {id}, Valor Total: {valor_total}, Descrição: {descricao}")

def adicionar_servico(session):
    # Coletar informações do usuário
    valor_total = float(input("Digite o valor total do serviço: "))  # Corrigimos para 'valor_total'
    descricao = input("Digite a descrição do serviço (opcional): ")
    
    # Criar uma nova instância de Servico
    novo_servico = Servico(valor_total=valor_total, descricao=descricao)  # Corrigimos para 'valor_total'
    
    # Adicionar o serviço à sessão
    session.add(novo_servico)
    
    try:
        # Commit para salvar no banco de dados
        session.commit()
        print("Serviço adicionado com sucesso!")
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao adicionar o serviço: {e}")



def executar():
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

if __name__ == "__main__":
    executar()
