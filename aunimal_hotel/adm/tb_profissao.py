from sqlalchemy import create_engine, Column, Integer, String, Float, Text, Date, ForeignKey, Enum, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('mysql://root:Brother25525&@localhost/aunimalhotel')
Session = sessionmaker(bind=engine)

# Crie uma instância da classe Base
Base = declarative_base()

class Profissao(Base):
    __tablename__ = "profissao"
    
    id_profissao = Column(Integer, primary_key=True, autoincrement=True)
    profissao = Column(String(50), nullable=False, unique=True)
    descricao = Column(Text, nullable=True)


def listar_profissoes(session):
    # Consultar todas as profissões disponíveis
    profissoes = session.query(Profissao).all()
    
    for profissao in profissoes:
        print(f"ID Profissão: {profissao.id_profissao}, Profissão: {profissao.profissao}, Descrição: {profissao.descricao}")

def adicionar_profissao(session):
    # Coletar informações da profissão
    profissao = input("Digite o nome da profissão: ")
    descricao = input("Digite a descrição da profissão (opcional): ")

    # Criar uma nova instância de Profissao
    nova_profissao = Profissao(profissao=profissao, descricao=descricao)

    try:
        # Adicionar a profissão à sessão e fazer o commit
        session.add(nova_profissao)
        session.commit()
        print("Profissão adicionada com sucesso!")
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao adicionar a profissão: {e}")

def remover_profissao(session):
    profissao_id = input("Digite o ID da profissão que deseja excluir: ")

    try:
        # Buscar a profissão pelo ID
        profissao = session.query(Profissao).filter(Profissao.id_profissao == profissao_id).one()

        # Remover a profissão
        session.delete(profissao)
        session.commit()
        print("Profissão excluída com sucesso!")
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao excluir a profissão: {e}")

def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar profissões")
        print("2. Adicionar profissão")
        print("3. Remover profissão")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_profissoes(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_profissao(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            remover_profissao(session)
        elif escolha == "4":
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
