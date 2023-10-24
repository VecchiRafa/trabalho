from tb_pessoa import Pessoa 
from sqlalchemy import DECIMAL, ForeignKey, DATETIME, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime
from services.conect_bd import Session, Base

#=============================================================================================================================================================
# Tabela funcionario
class Funcionario(Base):
    __tablename__ = "funcionario"

    id_funcionario: Mapped[int] = mapped_column("id_funcionario", INTEGER, ForeignKey(Pessoa.id_pessoa), primary_key=True, nullable=False, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    profissao: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    salario: Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)

#=============================================================================================================================================================
# Adicionar Funcionario

def adicionar_funcionario(session):
    nome = input("\nDigite o nome da pessoa: ")
    profissao = input("Digite a profissão do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    data_criacao = datetime.now()

    nova_pessoa = Pessoa(nome=nome, data_criacao=data_criacao)
    session.add(nova_pessoa)
    session.commit()

    novo_funcionario = Funcionario(id_funcionario=nova_pessoa.id_pessoa, data_criacao=data_criacao, profissao=profissao, salario=salario)
    session.add(novo_funcionario)
    session.commit()

    print("\nFuncionário adicionado com sucesso!")

#=============================================================================================================================================================
# Listar funcionarios

def listar_funcionario(session):
    funcionarios = session.query(Funcionario).all()
    for funcionario in funcionarios:
        print(f"\nID: {funcionario.id_funcionario} | Nome: {funcionario.pessoa.nome} | Profissão: {funcionario.profissao} | Salário: {funcionario.salario}")


#=============================================================================================================================================================
#Editar Funcionario

def editar_funcionario(session):
    print()
    listar_funcionario(session)
    funcionario_id = int(input("\nDigite o ID do funcionário que deseja editar: "))
    funcionario = session.query(Funcionario).get(funcionario_id)

    if funcionario:
        nome = input("Digite o novo nome da pessoa: ")
        profissao = input("Digite a nova profissão do funcionário: ")
        salario = float(input("Digite o novo salário do funcionário: "))

        funcionario.pessoa.nome = nome
        funcionario.profissao = profissao
        funcionario.salario = salario
        session.commit()

        print("\nFuncionário atualizado com sucesso!")
    else:
        print("\nFuncionário não encontrado.")


#=====================================================================================================================================
# Excluir funcionario

def excluir_funcionario(session):
    print()
    listar_funcionario(session)
    funcionario_id = int(input("\nDigite o ID do funcionário que deseja excluir: "))
    funcionario = session.query(Funcionario).get(funcionario_id)

    if funcionario:
        session.delete(funcionario)
        session.commit()
        print("Funcionário excluído com sucesso!")
    else:
        print("Funcionário não encontrado.")

#=====================================================================================================================================
def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar funcionario")
        print("2. Adicionar funcionario")
        print("3. Editar funcionario")
        print("4. Deletar funcionario")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_funcionario(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_funcionario(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            editar_funcionario(session)
        elif escolha == "4":
            print()
            print(50 * "=")
            print()
            excluir_funcionario(session)
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
