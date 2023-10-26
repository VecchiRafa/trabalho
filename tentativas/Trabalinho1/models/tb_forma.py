from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from services.conect_bd import Session, Base


class Forma(Base):
    __tablename__ = "forma"

    id_forma: Mapped[int] = mapped_column("id_forma", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    descricao: Mapped[str] = mapped_column(VARCHAR(50), nullable=True)


# Função para adicionar uma nova forma
def adicionar_forma(session):
    descricao = input("Digite a descrição da forma: ")
    nova_forma = Forma(descricao=descricao)
    session.add(nova_forma)
    session.commit()
    print("\nForma adicionada com sucesso!")

# Função para listar todas as formas
def listar_formas(session):
    formas = session.query(Forma).all()
    for forma in formas:
        print(f"\nID: {forma.id_forma} | Descrição: {forma.descricao}")

# Função para editar informações de uma forma
def editar_forma(session):
    print()
    listar_formas(session)
    forma_id = int(input("\nDigite o ID da forma que deseja editar: "))
    forma = session.query(Forma).get(forma_id)

    if forma:
        descricao = input("Digite a nova descrição da forma: ")
        forma.descricao = descricao
        session.commit()
        print("\nForma atualizada com sucesso!")
    else:
        print("\nForma não encontrada.")

# Função para excluir uma forma
def excluir_forma(session):
    print()
    listar_formas(session)
    forma_id = int(input("\nDigite o ID da forma que deseja excluir: "))
    forma = session.query(Forma).get(forma_id)

    if forma:
        session.delete(forma)
        session.commit()
        print("Forma excluída com sucesso!")
    else:
        print("Forma não encontrada.")

# Exemplos de uso:
def executar():

    session = Session()
    
    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar formas")
        print("2. Adicionar forma")
        print("3. Editar forma")
        print("4. Deletar forma")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_formas(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_forma(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            editar_forma(session)
        elif escolha == "4":
            print()
            print(50 * "=")
            print()
            excluir_forma(session)
        elif escolha == "5":
            print()
            print(50 * "=")
            print()
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar()
