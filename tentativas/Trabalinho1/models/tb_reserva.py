from services.conect_bd import Base, Session
from sqlalchemy import DATETIME, DECIMAL, VARCHAR, FLOAT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime
from tb_cliente import Cliente , listar_clientes
from tb_funcionario import Funcionario, listar_funcionario

class Reserva(Base):
    __tablename__ = "reserva"
    
    id_reserva: Mapped[int] = mapped_column("id_reserva", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    check_in: Mapped[datetime] = mapped_column(DATETIME,nullable=False,default=datetime.now())
    checkout: Mapped[datetime] = mapped_column(DATETIME,nullable=False,default=datetime.now())
    descricao: Mapped[str] = mapped_column(VARCHAR(200),nullable=True)
    valor_total: Mapped[float] = mapped_column(DECIMAL(10,2),nullable=False)
    id_cliente: Mapped[int] = mapped_column("id_cliente",INTEGER, ForeignKey(Cliente.id_cliente), nullable=False)
    id_funcionario: Mapped[int] = mapped_column("id_funcionario", INTEGER, ForeignKey(Funcionario.id_funcionario), nullable=False)

def adicionar_reserva(session):
    check_in = datetime.now()
    checkout = datetime.now()
    descricao = input("Digite uma descrição para a reserva: ")
    valor_total = float(input("Digite o valor total da reserva: "))
    print()
    listar_clientes(session)
    print()
    id_cliente = int(input("Digite o ID do cliente: "))
    print()
    listar_funcionario(session)
    print()
    id_funcionario = int(input("Digite o ID do funcionário: "))

    nova_reserva = Reserva(
        check_in=check_in,
        checkout=checkout,
        descricao=descricao,
        valor_total=valor_total,
        id_cliente=id_cliente,
        id_funcionario=id_funcionario
    )

    session.add(nova_reserva)
    session.commit()

    print("\nReserva adicionada com sucesso!")

def listar_reservas(session):
    reservas = session.query(Reserva).all()
    for reserva in reservas:
        print(f"\nID Reserva: {reserva.id_reserva} | Check-In: {reserva.check_in} | Check-Out: {reserva.checkout} | Descrição: {reserva.descricao} | Valor Total: {reserva.valor_total}")

def editar_reserva(session):
    print()
    listar_reservas(session)
    reserva_id = int(input("\nDigite o ID da reserva que deseja editar: "))
    reserva = session.get(Reserva, reserva_id)

    if reserva:
        descricao = input("Digite a nova descrição da reserva: ")
        valor_total = float(input("Digite o novo valor total da reserva: "))
        reserva.descricao = descricao
        reserva.valor_total = valor_total
        session.commit()

        print("\nReserva atualizada com sucesso!")
    else:
        print("\nReserva não encontrada.")

def excluir_reserva(session):
    print()
    listar_reservas(session)
    reserva_id = int(input("\nDigite o ID da reserva que deseja excluir: "))
    reserva = session.get(Reserva, reserva_id)

    if reserva:
        session.delete(reserva)
        session.commit()
        print("Reserva excluída com sucesso!")
    else:
        print("Reserva não encontrada.")

def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar reservas")
        print("2. Adicionar reserva")
        print("3. Editar reserva")
        print("4. Deletar reserva")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_reservas(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_reserva(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            editar_reserva(session)
        elif escolha == "4":
            print()
            print(50 * "=")
            print()
            excluir_reserva(session)
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