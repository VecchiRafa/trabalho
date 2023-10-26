from base import Base
from pessoa import Pessoa 
from sqlalchemy import ForeignKey, DATETIME
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime
from services.db import Session

class Cliente(Base):
    __tablename__ = "cliente"
    
    id_cliente: Mapped[int] = mapped_column("id_cliente", INTEGER, ForeignKey(Pessoa.id_pessoa), nullable=False, autoincrement=True, primary_key=True)
    id_pessoa: Mapped[int] = mapped_column("id_pessoa", INTEGER, ForeignKey(Pessoa.id_pessoa), nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())

    pessoa = relationship("Pessoa", back_populates="cliente", foreign_keys=[id_pessoa])
    
def tempo_cliente(data_criacao):
    data_atual = datetime.now()
    periodo_cliente = data_atual - data_criacao

    dias = periodo_cliente.days % 30
    meses = (periodo_cliente.days % 365) // 30  # Calcula o número de meses como parte inteira dos dias restantes divididos por 30
    anos = periodo_cliente.days // 365  # Calcula o número de anos como parte inteira dos dias divididos por 365

    return dias, meses, anos

 
def adicionar_cliente(session):
    nome = input("Digite o nome da pessoa: ")
    nascimento = input("Digite a data de nascimento (AAAA-MM-DD): ")
    cpf = input("Digite o CPF: ")
    rg = input("Digite o RG: ")
    sexo = input("Digite o sexo (M/F/NI): ")
    email = input("Digite o email: ")
    estado_civil = input("Digite o estado civil (SOLTEIRO, CASADO, DIVORCIADO, SEPARADO, VIUVO): ")
    nacionalidade = input("Digite a nacionalidade: ")
    data_criacao = datetime.now()
    
    # Criar uma nova instância de Pessoa
    nova_pessoa = Pessoa(nome=nome, nascimento=nascimento, cpf=cpf, rg=rg, sexo=sexo, email=email, est_civil=estado_civil,
                         nacionalidade=nacionalidade, data_criacao=data_criacao)
    
    try:
        # Adicionar a pessoa à sessão e fazer o commit para obter o ID gerado
        session.add(nova_pessoa)
        session.commit()

        # Obter o ID_pessoa recém-gerado
        id_pessoa = nova_pessoa.id_pessoa

        # Criar uma nova instância de Cliente associando à nova pessoa
        novo_cliente = Cliente(id_pessoa=id_pessoa)
        session.add(novo_cliente)
        session.commit()
        print("\n\nCliente adicionado com sucesso!")
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao adicionar o cliente: {e}")



def listar_clientes(session):
    print()

    # Consultar clientes e pessoas com informações combinadas
    clientes_pessoas = session.query(Cliente, Pessoa).filter(Cliente.id_pessoa == Pessoa.id_pessoa).all()
   
    for cliente, pessoa in clientes_pessoas:
        print(f"ID Cliente: {cliente.id_cliente} | Nome: {pessoa.nome} | CPF: {pessoa.cpf}, "
              f"Nascimento: {pessoa.nascimento} | Sexo: {pessoa.sexo} | Email: {pessoa.email} | estado civil: {pessoa.est_civil} ")


        
def deletar_cliente(session):
    listar_clientes(session)
    print()

    cliente_id = input("Digite o ID do cliente que deseja excluir: ")

    try:
        # Buscar o cliente pelo ID
        cliente = session.query(Cliente).filter(Cliente.id_cliente == cliente_id).one()

        # Remover o cliente
        session.delete(cliente)
        session.commit()
        print("Cliente excluído com sucesso!")
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao excluir o cliente: {e}")

def editar_cliente(session):
    listar_clientes(session)
    print()
    cliente_id = input("Digite o ID do cliente que deseja editar: ")

    try:
        cliente = session.query(Cliente).filter(Cliente.id_cliente == cliente_id).one()

        dados_pessoais = cliente.pessoa
        print(f"Informações atuais da pessoa:")
        print(f"Nome: {dados_pessoais.nome}")
        print(f"Nascimento: {dados_pessoais.nascimento}")
        print(f"CPF: {dados_pessoais.cpf}")
        print(f"RG: {dados_pessoais.rg}")
        print(f"Sexo: {dados_pessoais.sexo}")
        print(f"Email: {dados_pessoais.email}")
        print(f"Estado Civil: {dados_pessoais.est_civil}")
        print(f"Nacionalidade: {dados_pessoais.nacionalidade}")

        nome = input("Digite o novo nome da pessoa: ")
        nascimento = input("Digite a nova data de nascimento (AAAA-MM-DD): ")
        cpf = input("Digite o novo CPF: ")
        rg = input("Digite o novo RG: ")
        sexo = input("Digite o novo sexo (M/F/NI): ")
        email = input("Digite o novo email: ")
        est_civil = input("Digite o estado civil (SOLTEIRO, CASADO, DIVORCIADO, SEPARADO, VIÚVO): ")
        nacionalidade = input("Digite a nova nacionalidade: ")

        dados_pessoais.nome = nome
        dados_pessoais.nascimento = nascimento
        dados_pessoais.cpf = cpf
        dados_pessoais.rg = rg
        dados_pessoais.sexo = sexo
        dados_pessoais.email = email
        dados_pessoais.est_civil = est_civil
        dados_pessoais.nacionalidade = nacionalidade

        session.commit()
        print("Cliente atualizado com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao editar o cliente: {e}")

def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar clientes")
        print("2. Adicionar cliente")
        print("3. Editar cliente")
        print("4. Deletar cliente")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_clientes(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_cliente(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            editar_cliente(session)
        elif escolha == "4":
            print()
            print(50 * "=")
            print()
            deletar_cliente(session)
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
