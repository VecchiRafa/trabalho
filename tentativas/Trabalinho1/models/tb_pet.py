from services.conect_bd import Base, Session
from sqlalchemy import DATETIME, DECIMAL, VARCHAR, DATE, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime, date
from tb_especie import Especie, listar_especies
from tb_cliente import Cliente, listar_clientes

class Pet(Base):
    __tablename__ = "pet"

    id_pet: Mapped[int] = mapped_column("id_pet", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    nome: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    peso: Mapped[float] = mapped_column(DECIMAL(5,2), nullable=True)
    sexo: Mapped[Enum('M', 'F')] = mapped_column(Enum('M', 'F'), nullable=False)
    pelagem: Mapped[str] = mapped_column(VARCHAR(100), nullable=True)
    porte: Mapped[Enum('PP', 'P', 'M', 'G', 'GG')] = mapped_column(Enum('PP', 'P', 'M', 'G', 'GG'), nullable=False)
    nascimento: Mapped[date] = mapped_column(DATE, nullable=True)
    descricao: Mapped[str] = mapped_column(VARCHAR(200), nullable=True)
    id_especie: Mapped[int] = mapped_column("id_especie", INTEGER, ForeignKey(Especie.id_especie), primary_key=True, nullable=False) # chave PK Fk coloca junto?
    id_cliente: Mapped[int] = mapped_column("id_cliente", INTEGER, ForeignKey(Cliente.id_cliente), nullable=False)

def adicionar_pet(session):
    nome = input("Digite o nome do pet: ")
    peso = float(input("Digite o peso do pet (opcional, deixe em branco se não souber): "))
    sexo = input("Digite o sexo do pet (M ou F): ")
    pelagem = input("Digite a pelagem do pet (opcional, deixe em branco se não souber): ")
    porte = input("Digite o porte do pet (PP, P, M, G, ou GG): ")
    nascimento = input("Digite a data de nascimento do pet (AAAA-MM-DD, opcional, deixe em branco se não souber): ")
    descricao = input("Digite uma descrição para o pet (opcional, deixe em branco se não souber): ")

    
    # Listar os IDs de espécie
    listar_especies(session)
    print()
    id_especie = int(input("Digite o ID da espécie do pet: "))
    
    print()
    # Listar os IDs de clientes
    listar_clientes(session)
    print()
    id_cliente = int(input("Digite o ID do cliente do pet: "))

    nova_data_criacao = datetime.now()  # A data de criação é gerada automaticamente

    novo_pet = Pet(
        data_criacao=nova_data_criacao,
        nome=nome,
        peso=peso,
        sexo=sexo,
        pelagem=pelagem,
        porte=porte,
        nascimento=nascimento,
        descricao=descricao,
        id_especie=id_especie,
        id_cliente=id_cliente
    )

    session.add(novo_pet)
    session.commit()

    print("\nPet adicionado com sucesso!")

def listar_pets(session):
    pets = session.query(Pet).all()
    for pet in pets:
        print(f"\nID Pet: {pet.id_pet} | Nome: {pet.nome} | Sexo: {pet.sexo} | Porte: {pet.porte}")
        print(f"Data de Criação: {pet.data_criacao} | Peso: {pet.peso} | Pelagem: {pet.pelagem}")
        print(f"Nascimento: {pet.nascimento} | Descrição: {pet.descricao}")
        print(f"ID Espécie: {pet.id_especie} | ID Cliente: {pet.id_cliente}")

def editar_pet(session):
    print()
    listar_pets(session)
    pet_id = int(input("\nDigite o ID do pet que deseja editar: "))

    listar_especies(session)
    print()
    especie_id = int(input("Digite o ID da espécie do pet: "))

    pet = session.query(Pet).filter_by(id_pet=pet_id, id_especie=especie_id).first()

    if pet:
        nome = input("Digite o novo nome do pet: ")
        peso = float(input("Digite o novo peso do pet (opcional, deixe em branco se não souber): "))
        sexo = input("Digite o novo sexo do pet (M ou F): ")
        pelagem = input("Digite a nova pelagem do pet (opcional, deixe em branco se não souber): ")
        porte = input("Digite o novo porte do pet (PP, P, M, G, ou GG): ")
        nascimento = input("Digite a nova data de nascimento do pet (AAAA-MM-DD, opcional, deixe em branco se não souber): ")
        descricao = input("Digite uma nova descrição para o pet (opcional, deixe em branco se não souber): ")
        id_especie = int(input("Digite o novo ID da espécie do pet: "))
        id_cliente = int(input("Digite o novo ID do cliente do pet: "))

        pet.nome = nome
        pet.peso = peso
        pet.sexo = sexo
        pet.pelagem = pelagem
        pet.porte = porte
        pet.nascimento = nascimento
        pet.descricao = descricao
        pet.id_especie = id_especie
        pet.id_cliente = id_cliente
        session.commit()

        print("\nPet atualizado com sucesso!")
    else:
        print("\nPet não encontrado.")


def excluir_pet(session):
    print()
    listar_pets(session)
    pet_id = int(input("\nDigite o ID do pet que deseja excluir: "))
    especie_id = int(input("Digite o ID da espécie do pet: "))

    pet = session.query(Pet).filter_by(id_pet=pet_id, id_especie=especie_id).first()

    if pet:
        session.delete(pet)
        session.commit()
        print("Pet excluído com sucesso!")
    else:
        print("Pet não encontrado.")


def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar pets")
        print("2. Adicionar pet")
        print("3. Editar pet")
        print("4. Deletar pet")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_pets(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_pet(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            editar_pet(session)
        elif escolha == "4":
            print()
            print(50 * "=")
            print()
            excluir_pet(session)
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