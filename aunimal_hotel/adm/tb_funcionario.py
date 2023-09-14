from sqlalchemy import create_engine, Column, Integer, String, Float, Text, Date, ForeignKey, Enum, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Configuração da conexão com o banco de dados usando SQLAlchemy
engine = create_engine('mysql://root:Brother25525&@localhost/aunimalhotel')
Session = sessionmaker(bind=engine)

# Crie uma instância da classe Base
Base = declarative_base()

class Profissao(Base):
    __tablename__ = "profissao"
    
    id_profissao = Column(Integer, primary_key=True, autoincrement=True)
    profissao = Column(String(50), nullable=False, unique=True)
    descricao = Column(Text, nullable=True)

class Associado(Base):
    __tablename__ = "associado"
    
    id_associado = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    nascimento = Column(Date, nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    rg = Column(String(11), nullable=False, unique=True)
    sexo = Column(Enum('M', 'F', 'NI'), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    nacionalidade = Column(String(100), nullable=False, default='Brasil')
    data_criacao = Column(DateTime, nullable=False)

class Funcionario(Base):
    __tablename__ = "funcionario"
    
    id_funcionario = Column(Integer, primary_key=True, autoincrement=True)
    id_profissao = Column(Integer, ForeignKey('profissao.id_profissao'), nullable=False)
    data_admissao = Column(Date, nullable=False)
    salario = Column(Float, nullable=False)
    estado_civil = Column(String(20), nullable=False)
    id_associado = Column(Integer, ForeignKey('associado.id_associado'), nullable=False)
    
    # Adicionar relacionamentos para acessar os dados da profissão, associado
    profissao = relationship('Profissao', backref='funcionario')
    associado = relationship('Associado', backref='funcionario')

    def __init__(self, id_profissao, data_admissao, salario, estado_civil, id_associado):
        self.id_profissao = id_profissao
        self.data_admissao = data_admissao
        self.salario = salario
        self.estado_civil = estado_civil
        self.id_associado = id_associado

def listar_profissoes(session):
    # Consultar todas as profissões disponíveis
    profissoes = session.query(Profissao).all()
    
    for profissao in profissoes:
        print(f"ID Profissão: {profissao.id_profissao}, Profissão: {profissao.profissao}, Descrição: {profissao.descricao}")


def listar_funcionarios(session):
    # Consultar funcionários com informações de profissões e associados
    funcionarios = session.query(Funcionario, Profissao, Associado).join(Profissao).join(Associado).all()
    
    for funcionario, profissao, associado in funcionarios:
        print(f"ID Funcionário: {funcionario.id_funcionario}, "
              f"Profissão: {profissao.profissao}, "
              f"Data Admissão: {funcionario.data_admissao}, "
              f"Salário: {funcionario.salario}, "
              f"Estado Civil: {funcionario.estado_civil}, "
              f"ID Associado: {associado.id_associado}, "
              f"Nome Associado: {associado.nome}, "
              f"Nascimento Associado: {associado.nascimento}, "
              f"CPF Associado: {associado.cpf}, "
              f"RG Associado: {associado.rg}, "
              f"Sexo Associado: {associado.sexo}, "
              f"Email Associado: {associado.email}")

def adicionar_funcionario(session):
    # Coletar informações do funcionário
    salario = float(input("Digite o salário: "))
    estado_civil = input("Digite o estado civil: ")

    # Perguntar se o funcionário já é um associado
    is_associado = input("O funcionário já é um associado? (S/N): ").strip().lower()

    if is_associado == "s":
        # Coletar informações do associado existente
        listar_associados(session)
        associado_id = input("Digite o ID do associado existente: ")
    else:
        # Coletar informações do novo associado
        nome = input("Digite o nome do associado: ")
        nascimento = input("Digite a data de nascimento (AAAA-MM-DD): ")

        # Verificar o CPF
        while True:
            cpf = input("Digite o CPF (11 dígitos): ")
            if len(cpf) == 11 and cpf.isdigit():
                break
            else:
                print("CPF inválido. O CPF deve conter exatamente 11 dígitos numéricos.")

        rg = input("Digite o RG: ")
        sexo = input("Digite o sexo (M/F/NI): ")
        email = input("Digite o email: ")
        nacionalidade = input("Digite a nacionalidade: ")
        
        # Criar uma nova instância de Associado
        novo_associado = Associado(nome=nome, nascimento=nascimento, cpf=cpf, rg=rg, sexo=sexo, email=email,
                                   nacionalidade=nacionalidade, data_criacao=datetime.now())
        
        try:
            # Adicionar o novo associado à sessão e fazer o commit para obter o ID gerado
            session.add(novo_associado)
            session.commit()
            
            # Obter o ID_associado recém-gerado
            associado_id = novo_associado.id_associado
            print(f"Associado adicionado com sucesso. ID Associado: {associado_id}")
        except Exception as e:
            # Em caso de erro, faça o rollback e mostre a mensagem de erro
            session.rollback()
            print(f"Erro ao adicionar o associado: {e}")

    # Coletar informações da profissão disponível
    listar_profissoes(session)
    profissao_id = input("Digite o ID da profissão desejada: ")

    # Criar uma nova instância de Funcionario
    novo_funcionario = Funcionario(id_profissao=profissao_id, data_admissao=datetime.now(), salario=salario, estado_civil=estado_civil,
                                   id_associado=associado_id)

    try:
        # Adicionar o funcionário à sessão e fazer o commit
        session.add(novo_funcionario)
        session.commit()
        print("Funcionário adicionado com sucesso!")
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao adicionar o funcionário: {e}")


    # Coletar informações da profissão disponível
    listar_profissoes(session)
    profissao_id = input("Digite o ID da profissão desejada: ")

    # Criar uma nova instância de Funcionario
    novo_funcionario = Funcionario(id_profissao=profissao_id, data_admissao=datetime.now(), salario=salario, estado_civil=estado_civil,
                                   id_associado=associado_id)

    try:
        # Adicionar o funcionário à sessão e fazer o commit
        session.add(novo_funcionario)
        session.commit()
        print("Funcionário adicionado com sucesso!")
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao adicionar o funcionário: {e}")


def remover_funcionario(session):
    try:
        # Consultar funcionários
        funcionarios = session.query(Funcionario).all()
        
        if not funcionarios:
            print("Não há funcionários para excluir.")
            return

        print("Funcionários disponíveis para exclusão:")
        for funcionario in funcionarios:
            print(f"ID Funcionário: {funcionario.id_funcionario}, Nome: {funcionario.associado.nome}")

        funcionario_id = input("Digite o ID do funcionário que deseja excluir ou '0' para cancelar: ")

        if funcionario_id == '0':
            print("Operação de exclusão cancelada.")
        else:
            try:
                # Buscar o funcionário pelo ID
                funcionario = session.query(Funcionario).filter(Funcionario.id_funcionario == funcionario_id).one()

                # Remover o funcionário
                session.delete(funcionario)
                session.commit()
                print("Funcionário excluído com sucesso!")
            except Exception as e:
                # Em caso de erro, faça o rollback e mostre a mensagem de erro
                session.rollback()
                print(f"Erro ao excluir o funcionário: {e}")
    except Exception as e:
        print(f"Erro ao listar funcionários: {e}")


def listar_associados(session):
    # Consultar todos os associados disponíveis
    associados = session.query(Associado).all()

    for associado in associados:
        print(f"ID Associado: {associado.id_associado}, "
              f"Nome: {associado.nome}, "
              f"Nascimento: {associado.nascimento}, "
              f"CPF: {associado.cpf}, "
              f"RG: {associado.rg}, "
              f"Sexo: {associado.sexo}, "
              f"Email: {associado.email}")

def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar funcionários")
        print("2. Adicionar funcionário")
        print("3. Remover funcionário")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_funcionarios(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_funcionario(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            remover_funcionario(session)
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
