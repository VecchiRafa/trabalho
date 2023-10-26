from services.conect_bd import Base, Session
from sqlalchemy import DECIMAL, ForeignKey, DATETIME
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime
from tb_funcionario import Funcionario, listar_funcionario
from tb_reserva import Reserva, listar_reservas

class Cobranca(Base):
    __tablename__ = "cobranca"

    id_cobranca: Mapped[int] = mapped_column("id_cobranca", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    data_cobranca: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    valor_total: Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)
    id_reserva: Mapped[int] = mapped_column("id_reserva", INTEGER, ForeignKey(Reserva.id_reserva), nullable=False)
    id_funcionario: Mapped[int] = mapped_column("id_funcionario", INTEGER, ForeignKey(Funcionario.id_funcionario), nullable=False)


def adicionar_cobranca(session):
    data_cobranca = datetime.now()
    valor_total = float(input("Digite o valor total da cobrança: "))

    listar_reservas(session)
    print()
    id_reserva = int(input("Digite o ID da reserva: "))

    listar_funcionario(session)
    print()
    id_funcionario = int(input("Digite o ID do funcionário: "))

    nova_cobranca = Cobranca(
        data_cobranca=data_cobranca,
        valor_total=valor_total,
        id_reserva=id_reserva,
        id_funcionario=id_funcionario
    )

    session.add(nova_cobranca)
    session.commit()

    print("\nCobrança adicionada com sucesso!")

def listar_cobrancas(session):
    cobrancas = session.query(Cobranca).all()
    for cobranca in cobrancas:
        print(f"\nID Cobrança: {cobranca.id_cobranca} | Data Cobrança: {cobranca.data_cobranca} | Valor Total: {cobranca.valor_total} |"
              f"ID Reserva: {cobranca.id_reserva} | ID Funcionário: {cobranca.id_funcionario}")

def editar_cobranca(session):
    print()
    listar_cobrancas(session)
    cobranca_id = int(input("\nDigite o ID da cobrança que deseja editar: "))
    cobranca = session.get(Cobranca, cobranca_id)

    if cobranca:
        valor_total = float(input("Digite o novo valor total da cobrança: "))

        # Adicione as linhas abaixo para editar os atributos adicionais
        data_cobranca = datetime.now()

        listar_reservas(session)
        print()
        id_reserva = int(input("Digite o ID da reserva: "))

        listar_funcionario(session)
        print()
        id_funcionario = int(input("Digite o ID do funcionário: "))

        cobranca.valor_total = valor_total
        cobranca.data_cobranca = data_cobranca
        cobranca.id_reserva = id_reserva
        cobranca.id_funcionario = id_funcionario

        session.commit()

        print("\nCobrança atualizada com sucesso!")
    else:
        print("\nCobrança não encontrada.")

def excluir_cobranca(session):
    print()
    listar_cobrancas(session)
    cobranca_id = int(input("\nDigite o ID da cobrança que deseja excluir: "))
    cobranca = session.get(Cobranca, cobranca_id)

    if cobranca:
        session.delete(cobranca)
        session.commit()
        print("Cobrança excluída com sucesso!")
    else:
        print("Cobrança não encontrada.")

def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar cobranças")
        print("2. Adicionar cobrança")
        print("3. Editar cobrança")
        print("4. Deletar cobrança")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_cobrancas(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_cobranca(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            editar_cobranca(session)
        elif escolha == "4":
            print()
            print(50 * "=")
            print()
            excluir_cobranca(session)
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