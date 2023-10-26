# ver a questão das tb muito pra muitos

from services.conect_bd import Base, Session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from tb_pet import Pet, listar_pets
from tb_servico import Servico, listar_servico


class Pet_servico(Base):
    __tablename__ = "pet_servico"

    id_pet: Mapped[int] = mapped_column("id_pet", INTEGER, ForeignKey(Pet.id_pet), primary_key=True, nullable=False) 
    id_servico: Mapped[int] = mapped_column("id_servico", INTEGER, ForeignKey(Servico.id_servico), primary_key=True, nullable=False) 

def adicionar_pet_servico(session):
    listar_pets(session)
    pet_id = int(input("Digite o ID do pet: "))

    listar_servico(session)
    servico_id = int(input("Digite o ID do serviço: "))

    novo_pet_servico = Pet_servico(id_pet=pet_id, id_servico=servico_id)
    session.add(novo_pet_servico)
    session.commit()
    print("\nAssociação pet-serviço adicionada com sucesso!")

def listar_pet_servico(session):
    pet_servicos = session.query(Pet_servico).all()
    for pet_servico in pet_servicos:
        print(f"ID Pet: {pet_servico.id_pet} | ID Serviço: {pet_servico.id_servico}")

def editar_pet_servico(session):
    listar_pet_servico(session)
    pet_id = int(input("\nDigite o ID do pet da associação que deseja editar: "))
    servico_id = int(input("Digite o ID do serviço da associação que deseja editar: "))

    pet_servico = session.query(Pet_servico).filter_by(id_pet=pet_id, id_servico=servico_id).first()
    if pet_servico:
        # Você pode adicionar o código para editar campos adicionais, se necessário.
        session.commit()
        print("\nAssociação pet-serviço atualizada com sucesso!")
    else:
        print("\nAssociação pet-serviço não encontrada.")

def excluir_pet_servico(session):
    listar_pet_servico(session)
    pet_id = int(input("\nDigite o ID do pet da associação que deseja excluir: "))
    servico_id = int(input("Digite o ID do serviço da associação que deseja excluir: "))

    pet_servico = session.query(Pet_servico).filter_by(id_pet=pet_id, id_servico=servico_id).first()
    if pet_servico:
        session.delete(pet_servico)
        session.commit()
        print("\nAssociação pet-serviço excluída com sucesso!")
    else:
        print("\nAssociação pet-serviço não encontrada.")

def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar associações Pet-Serviço")
        print("2. Adicionar associação Pet-Serviço")
        print("3. Editar associação Pet-Serviço")
        print("4. Excluir associação Pet-Serviço")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_pet_servico(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_pet_servico(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            editar_pet_servico(session)
        elif escolha == "4":
            print()
            print(50 * "=")
            print()
            excluir_pet_servico(session)
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