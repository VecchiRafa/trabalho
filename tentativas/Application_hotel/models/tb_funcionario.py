from tb_pessoa import Pessoa, adicionar_pessoa
from sqlalchemy import DECIMAL, ForeignKey, DATETIME, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column, joinedload, relationship
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
    
    pessoa = relationship("Pessoa")

#=============================================================================================================================================================
# Adicionar Funcionario

def adicionar_funcionario(session):
    from tb_pessoa import adicionar_pessoa
    nova_pessoa = adicionar_pessoa(session)
    profissao = input("Digite a profissão do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))

    novo_funcionario = Funcionario(
        id_funcionario=nova_pessoa.id_pessoa,
        profissao=profissao,
        salario=salario
    )

    session.add(novo_funcionario)
    session.commit()

    print("\nFuncionário adicionado com sucesso!")

# Função para listar todos os funcionários
def listar_funcionario(session):
    # Consultar funcionários e informações da tabela Pessoa combinadas
    funcionarios_pessoas = session.query(Funcionario, Pessoa).filter(Funcionario.id_funcionario == Pessoa.id_pessoa).all()
    
    if funcionarios_pessoas:
        print("\nLista de Funcionários:")
        for funcionario, pessoa in funcionarios_pessoas:
            print(f"ID Funcionário: {funcionario.id_funcionario} | Nome: {pessoa.nome} | Profissão: {funcionario.profissao} | Salário: {funcionario.salario}")
    else:
        print("Nenhum funcionário encontrado.")

# Função para editar informações de um funcionário
def editar_funcionario(session):
    print()
    listar_funcionario(session)
    funcionario_id = int(input("\nDigite o ID do funcionário que deseja editar: "))
    funcionario = session.query(Funcionario).filter_by(id_funcionario=funcionario_id).first()

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

# Função para excluir um funcionário
def excluir_funcionario(session):
    print()
    listar_funcionario(session)
    funcionario_id = int(input("\nDigite o ID do funcionário que deseja excluir: "))
    funcionario = session.query(Funcionario).filter_by(id_funcionario=funcionario_id).first()

    if funcionario:
        session.delete(funcionario)
        session.commit()
        print("Funcionário excluído com sucesso!")
    else:
        print("Funcionário não encontrado.")

# Função principal para executar o programa
def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar funcionário")
        print("2. Adicionar funcionário")
        print("3. Editar funcionário")
        print("4. Deletar funcionário")
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