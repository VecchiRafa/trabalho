# arrumar, não tem editar nem excluir

from services.conect_bd import Base
from tb_pessoa import Pessoa , listar_pessoa
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy import ForeignKey
from services.conect_bd import Session

#=============================================================================================


class Contato(Base):
    __tablename__ = "contato"

    codigo_pais: Mapped[int] = mapped_column(TINYINT(3, unsigned=True, zerofill=True), nullable=False)
    codigo_area: Mapped[int] = mapped_column(TINYINT(unsigned=True), nullable=False)
    numero: Mapped[int] = mapped_column(INTEGER(unsigned=True), primary_key=True, nullable=False)
    id_pessoa: Mapped[int] = mapped_column("id_pessoa", INTEGER, ForeignKey(Pessoa.id_pessoa), primary_key=True, nullable=False)

#=============================================================================================
# Adicionar Contato

def adicionar_contato(session):
    codigo_pais = int(input("\nDigite o código do país: "))
    codigo_area = int(input("Digite o código da área: "))
    numero = int(input("Digite o número de contato: "))

    # ID da pessoa associada ao contato
    print()
    listar_pessoa(session)
    print()
    id_pessoa = int(input("Digite o ID da pessoa associada a este contato: "))

    novo_contato = Contato(
        codigo_pais=codigo_pais,
        codigo_area=codigo_area,
        numero=numero,
        id_pessoa=id_pessoa
    )

    session.add(novo_contato)
    session.commit()

    print("\nContato adicionado com sucesso!")

#=============================================================================================
# Listar contatos

def listar_contatos(session):
    contatos = session.query(Contato).all()
    for contato in contatos:
        print(f"\nCódigo do País: {contato.codigo_pais} | Código de Área: {contato.codigo_area} | Número de Contato: {contato.numero} | ID da Pessoa: {contato.id_pessoa}")

#=============================================================================================
# Editar Contato

def editar_contato(session):
    print()
    listar_contatos(session)
    contato_id = int(input("\nDigite o ID do contato que deseja editar: "))
    contato = session.query(Contato).get(contato_id)

    if contato:
        codigo_pais = int(input("Digite o novo código do país: "))
        codigo_area = int(input("Digite o novo código da área: "))
        numero = int(input("Digite o novo número de contato: "))
        id_pessoa = int(input("Digite o novo ID da pessoa associada a este contato: "))

        contato.codigo_pais = codigo_pais
        contato.codigo_area = codigo_area
        contato.numero = numero
        contato.id_pessoa = id_pessoa

        session.commit()

        print("\nContato atualizado com sucesso!")
    else:
        print("\nContato não encontrado.")

#=============================================================================================
# Excluir Contato

def excluir_contato(session):
    print()
    listar_contatos(session)
    contato_id = int(input("\nDigite o ID do contato que deseja excluir: "))
    contato = session.query(Contato).get(contato_id)

    if contato:
        session.delete(contato)
        session.commit()
        print("Contato excluído com sucesso!")
    else:
        print("Contato não encontrado.")

#=============================================================================================
def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar contatos")
        print("2. Adicionar contato")
        print("3. Editar contato")
        print("4. Deletar contato")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_contatos(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_contato(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            editar_contato(session)
        elif escolha == "4":
            print()
            print(50 * "=")
            print()
            excluir_contato(session)
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
