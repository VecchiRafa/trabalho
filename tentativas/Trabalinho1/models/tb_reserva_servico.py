from services.conect_bd import Base, Session
from sqlalchemy import DATETIME, DECIMAL, VARCHAR, INTEGER, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from tb_reserva import Reserva, listar_reservas
from tb_servico import Servico, listar_servico

class Reserva_servico(Base):
    __tablename__ = "reserva_servico"

    id_reserva: Mapped[int] = mapped_column("id_reserva", INTEGER, ForeignKey(Reserva.id_reserva), primary_key=True, nullable=False) 
    id_servico: Mapped[int] = mapped_column("id_servico", INTEGER, ForeignKey(Servico.id_servico), primary_key=True, nullable=False)

# Adicionar reserva a um serviço
def adicionar_reserva_servico(session):
    while True:
        print("Escolha uma reserva para vincular ao serviço:")
        listar_reservas(session)
        reserva_id = int(input("Digite o ID da reserva: "))

        reserva = session.get(Reserva, reserva_id)
        if reserva:
            break
        else:
            print("Reserva não encontrada. Tente novamente.")

    while True:
        print("Escolha um serviço para vincular à reserva:")
        listar_servico(session)
        servico_id = int(input("Digite o ID do serviço: "))

        servico = session.get(Servico, servico_id)
        if servico:
            break
        else:
            print("Serviço não encontrado. Tente novamente.")

    nova_reserva_servico = Reserva_servico(id_reserva=reserva_id, id_servico=servico_id)
    session.add(nova_reserva_servico)
    session.commit()
    print("Reserva vinculada ao serviço com sucesso!")

# Listar todas as associações entre Reserva e Servico
def listar_reservas_servico(session):
    reservas_servico = session.query(Reserva_servico).all()
    for reserva_servico in reservas_servico:
        print(f"ID Reserva: {reserva_servico.id_reserva} | ID Servico: {reserva_servico.id_servico}")

# Remover uma associação entre Reserva e Servico
def excluir_reserva_servico(session):
    print("Escolha a associação que deseja excluir:")
    listar_reservas_servico(session)
    reserva_id = int(input("Digite o ID da reserva: "))
    servico_id = int(input("Digite o ID do serviço:"))

    reserva_servico = session.query(Reserva_servico).filter_by(id_reserva=reserva_id, id_servico=servico_id).first()
    if reserva_servico:
        session.delete(reserva_servico)
        session.commit()
        print("Associação entre reserva e serviço excluída com sucesso!")
    else:
        print("Associação não encontrada.")

def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar associações Reserva e Serviço")
        print("2. Adicionar associação Reserva e Serviço")
        print("3. Excluir associação Reserva e Serviço")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_reservas_servico(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_reserva_servico(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            excluir_reserva_servico(session)
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
