from sqlalchemy import DATETIME, DATE, VARCHAR, CHAR, Enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime, date
from services.conect_bd import Session, Base


#==========================================================================================================================================================================
# tabela pessoas

class Pessoa(Base):
    __tablename__ = "pessoa"
    __table_args__ = {'extend_existing': True}
    
    id_pessoa: Mapped[int] = mapped_column("id_pessoa", INTEGER,nullable=False, autoincrement=True, primary_key=True)
    nome: Mapped[str] =  mapped_column(VARCHAR(100), nullable=False)
    nascimento: Mapped[date] = mapped_column(DATE, nullable=False)
    cpf: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True)
    rg: Mapped[str] = mapped_column(CHAR(11), nullable=False, unique=True)
    sexo: Mapped[Enum('M','F','NI')] = mapped_column(CHAR(2), nullable=False)
    email: Mapped[str] = mapped_column(VARCHAR(50), nullable=False, unique=True)
    est_civil: Mapped[str] =  mapped_column(VARCHAR(100), nullable=False)
    nacionalidade: Mapped[str] = mapped_column(VARCHAR(100), nullable=False, default='Brasil')
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now(), onupdate=datetime.now())

    

#==========================================================================================================================================================================
# listar pessoa.

def listar_pessoa(session):
    # Consultar pessoas
    pessoas = session.query(Pessoa).all()

    for pessoa in pessoas:
        print(
            f"\nID: {pessoa.id_pessoa} | Nome: {pessoa.nome} | Nascimento: {pessoa.nascimento} | CPF: {pessoa.cpf} | RG: {pessoa.rg} | "
            f"Sexo: {pessoa.sexo} | Email: {pessoa.email} | Estado Civil: {pessoa.est_civil} | Nacionalidade: {pessoa.nacionalidade} | "
            f"Data de Criação: {pessoa.data_criacao}"
        )

#==========================================================================================================================================================================
# adicionar pessoa.


def adicionar_pessoa(session):
    nome = input("Nome: ")
    nascimento = input("Data de Nascimento (AAAA-MM-DD): ")
    cpf = input("CPF: ")
    pessoa_existente = session.query(Pessoa).filter_by(cpf=cpf).first()

    if pessoa_existente:
        print("Um registro com este CPF já existe na tabela de pessoas.")
        return pessoa_existente
    
    rg = input("RG: ")
    sexo = input("Sexo (M/F/NI): ")
    email = input("Email: ")

    # Verifique se o email já existe na tabela de pessoas
    pessoa_existente = session.query(Pessoa).filter_by(email=email).first()

    if pessoa_existente:
        print("Um registro com este email já existe na tabela de pessoas.")
        return pessoa_existente  # Retornar a pessoa existente

    est_civil = input("Estado Civil (SOLTEIRO/CASADO/DIVORCIADO/SEPARADO/VIUVO): ")
    nacionalidade = input("Nacionalidade (Opcional, pressione Enter para usar 'Brasil'): ")

    nova_pessoa = Pessoa(
        nome=nome,
        nascimento=nascimento,
        cpf=cpf,
        rg=rg,
        sexo=sexo,
        email=email,
        est_civil=est_civil,
        nacionalidade=nacionalidade if nacionalidade else 'Brasil'
    )

    session.add(nova_pessoa)
    session.commit()

    print("Pessoa adicionada com sucesso.")

    # Agora, você pode chamar as funções de adicionar_contato e adicionar_endereco
    id_pessoa = nova_pessoa.id_pessoa
    from tb_cliente import Cliente
    novo_cliente = Cliente(id_pessoa=id_pessoa)
    session.add(novo_cliente)
    session.commit()

    from tb_contato import adicionar_contato
    from tb_endereco import adicionar_endereco

    adicionar_endereco(session, id_pessoa)
    adicionar_contato(session, id_pessoa)

    return nova_pessoa
#==========================================================================================================================================================================
# editar pessoa

def editar_pessoa(session):
    listar_pessoa(session)
    pessoa_id = int(input("Digite o ID da pessoa que deseja editar: "))
    nome = input("Novo Nome: ")
    nascimento = input("Nova Data de Nascimento (AAAA-MM-DD): ")
    cpf = input("Novo CPF: ")
    rg = input("Novo RG: ")
    sexo = input("Novo Sexo (M/F/NI): ")
    email = input("Novo Email: ")
    est_civil = input("Novo Estado Civil (SOLTEIRO/CASADO/DIVORCIADO/SEPARADO/VIUVO): ")
    nacionalidade = input("Nova Nacionalidade (Opcional, pressione Enter para manter a atual): ")

    pessoa = session.query(Pessoa).filter_by(id_pessoa=pessoa_id).first()
    if pessoa:
        pessoa.nome = nome
        pessoa.nascimento = nascimento
        pessoa.cpf = cpf
        pessoa.rg = rg
        pessoa.sexo = sexo
        pessoa.email = email
        pessoa.est_civil = est_civil
        pessoa.nacionalidade = nacionalidade
        session.commit()
        print("Informações da pessoa atualizadas com sucesso.")
    else:
        print(f"Pessoa com ID {pessoa_id} não encontrada.")

#==========================================================================================================================================================================
# Deletar usuario.

def deletar_pessoa(session):
    listar_pessoa(session)
    pessoa_id = int(input("Digite o ID da pessoa que deseja deletar: "))

    pessoa = session.query(Pessoa).filter_by(id_pessoa=pessoa_id).first()
    if pessoa:
        session.delete(pessoa)
        session.commit()
        print("Pessoa deletada com sucesso.")
    else:
        print(f"Pessoa com ID {pessoa_id} não encontrada.")


#==========================================================================================================================================================================
# Menu de opções.

def executar():
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar pessoas")
        print("2. Adicionar pessoa")
        print("3. Editar pessoa")
        print("4. Deletar pessoa")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listar_pessoa(session)
        elif escolha == "2":
            adicionar_pessoa(session)
        elif escolha == "3":
            editar_pessoa(session)
        elif escolha == "4":
            deletar_pessoa(session)
        elif escolha == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

    session.close()

if __name__ == "__main__":
    executar()