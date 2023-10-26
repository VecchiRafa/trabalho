from services.conect_bd import Base, Session
from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER


class Raca(Base):
    __tablename__ = "raca"

    id_raca: Mapped[int] = mapped_column("id_raca", INTEGER, nullable=False, primary_key=True, autoincrement=True)
    classificacao: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)

def adicionar_raca(session):
    classificacao = input("Digite a classificação da raça: ")

    nova_raca = Raca(
        classificacao=classificacao
    )

    session.add(nova_raca)
    session.commit()

    print("\nRaça adicionada com sucesso!")

def listar_racas(session):
    racas = session.query(Raca).all()
    for raca in racas:
        print(f"\nID Raça: {raca.id_raca} | Classificação: {raca.classificacao}")

def editar_raca(session):
    print()
    listar_racas(session)
    raca_id = int(input("\nDigite o ID da raça que deseja editar: "))
    raca = session.get(Raca, raca_id)

    if raca:
        classificacao = input("Digite a nova classificação da raça: ")
        raca.classificacao = classificacao
        session.commit()

        print("\nRaça atualizada com sucesso!")
    else:
        print("\nRaça não encontrada.")

def excluir_raca(session):
    print()
    listar_racas(session)
    raca_id = int(input("\nDigite o ID da raça que deseja excluir: "))
    raca = session.get(Raca, raca_id)

    if raca:
        session.delete(raca)
        session.commit()
        print("Raça excluída com sucesso!")
    else:
        print("Raça não encontrada.")

def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar raças")
        print("2. Adicionar raça")
        print("3. Editar raça")
        print("4. Deletar raça")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_racas(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_raca(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            editar_raca(session)
        elif escolha == "4":
            print()
            print(50 * "=")
            print()
            excluir_raca(session)
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