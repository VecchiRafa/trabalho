from services.conect_bd import Base, Session
from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from tb_raca import Raca, listar_racas

class Especie(Base):
    __tablename__ = "especie"

    id_especie: Mapped[int] = mapped_column("id_especie", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    tipo: Mapped[Enum('GATO','CACHORRO')] = mapped_column(Enum('GATO','CACHORRO'), nullable=False)
    id_raca: Mapped[int] = mapped_column("id_raca", INTEGER, ForeignKey(Raca.id_raca), autoincrement=True, nullable=False)

def adicionar_especie(session):
    tipo = input("Digite o tipo de espécie (GATO ou CACHORRO): ")
    
    # Listar os IDs de raças
    listar_racas(session)
    
    id_raca = int(input("Digite o ID da raça: "))
    
    nova_especie = Especie(
        tipo=tipo,
        id_raca=id_raca
    )

    session.add(nova_especie)
    session.commit()

    print("\nEspécie adicionada com sucesso!")

def listar_especies(session):
    especies = session.query(Especie).all()
    for especie in especies:
        print(f"\nID Espécie: {especie.id_especie} | Tipo: {especie.tipo} | ID Raça: {especie.id_raca}")

def editar_especie(session):
    print()
    listar_especies(session)
    especie_id = int(input("\nDigite o ID da espécie que deseja editar: "))
    especie = session.get(Especie, especie_id)

    if especie:
        tipo = input("Digite o novo tipo da espécie (GATO ou CACHORRO): ")
        id_raca = int(input("Digite o novo ID da raça: "))
        especie.tipo = tipo
        especie.id_raca = id_raca
        session.commit()

        print("\nEspécie atualizada com sucesso!")
    else:
        print("\nEspécie não encontrada.")

def excluir_especie(session):
    print()
    listar_especies(session)
    especie_id = int(input("\nDigite o ID da espécie que deseja excluir: "))
    especie = session.get(Especie, especie_id)

    if especie:
        session.delete(especie)
        session.commit()
        print("Espécie excluída com sucesso!")
    else:
        print("Espécie não encontrada.")

def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar espécies")
        print("2. Adicionar espécie")
        print("3. Editar espécie")
        print("4. Deletar espécie")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_especies(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_especie(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            editar_especie(session)
        elif escolha == "4":
            print()
            print(50 * "=")
            print()
            excluir_especie(session)
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