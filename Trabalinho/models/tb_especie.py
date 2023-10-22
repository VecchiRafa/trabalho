from sqlalchemy import create_engine, Column, Integer, Enum, ForeignKey, String
from sqlalchemy.orm import relationship
from services.conect_bd import Session, Base


# tabela especie:

class Especie(Base):
    __tablename__ = "especie"
    
    id_especie = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(30), nullable=False)
    id_raca = Column(Integer, ForeignKey('raca.id_raca'), nullable=False)

    # Remove a relação de volta 'raca' da classe 'Especie'
    
    def __init__(self, tipo, id_raca):
        self.tipo = tipo
        self.id_raca = id_raca

# tabela raça:

class Raca(Base):
    __tablename__ = "raca" 

    id_raca = Column(Integer, primary_key=True, autoincrement=True)
    classificacao = Column(String(100), nullable=False)

    # Adicione um relacionamento para acessar os dados da espécie
    especies = relationship('Especie', backref='raca')

    def __init__(self, classificacao):
        self.classificacao = classificacao

# inicio CRUD tabela especie

def adicionar_especie(session):
    tipo = input("Digite o tipo de espécie (GATO ou CACHORRO): ")
    id_raca = int(input("Digite o ID da raça associada a esta espécie: "))
    
    # Criar uma nova instância de Especie
    nova_especie = Especie(tipo=tipo, id_raca=id_raca)
    
    try:
        # Adicionar a espécie à sessão e fazer o commit para obter o ID gerado
        session.add(nova_especie)
        session.commit()
        
        print("Espécie adicionada com sucesso!")
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao adicionar a espécie: {e}")
#========================================================================================================
#listar especies.

def listar_especies(session):  
    especies = session.query(Especie).all()
    
    for especie in especies:
        print(f"ID Espécie: {especie.id_especie} | Tipo: {especie.tipo} | ID Raça: {especie.id_raca}")

#========================================================================================================

def deletar_especie(session):
    listar_especies(session)
    print()

    especie_id = int(input("Digite o ID da espécie que deseja excluir: "))

    try:
        # Buscar a espécie pelo ID
        especie = session.query(Especie).filter(Especie.id_especie == especie_id).one()

        # Remover a espécie
        session.delete(especie)
        session.commit()
        print("Espécie excluída com sucesso!")
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao excluir a espécie: {e}")

def editar_especie(session):
    
    listar_especies(session)
    print()
    especie_id = int(input("Digite o ID da espécie que deseja editar: "))

    try:
        # Buscar a espécie pelo ID
        especie = session.query(Especie).filter(Especie.id_especie == especie_id).one()

        tipo = input("Digite o novo tipo de espécie (GATO ou CACHORRO): ")
        id_raca = int(input("Digite o novo ID da raça associada a esta espécie: "))

        # Atualizar as informações da espécie
        especie.tipo = tipo
        especie.id_raca = id_raca

        session.commit()
        print("Espécie atualizada com sucesso!")
    except Exception as e:
        # Em caso de erro, faça o rollback e mostre a mensagem de erro
        session.rollback()
        print(f"Erro ao editar a espécie: {e}")
# fim do CRUD da Tabela especie 

# inicio da tabela raça

def adicionar_raca(session):
    classificacao = input("Digite a classificação da raça: ")

    nova_raca = Raca(classificacao=classificacao)

    try:
        session.add(nova_raca)
        session.commit()
        print("Raça adicionada com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao adicionar a raça: {e}")

def listar_racas(session):
    racas = session.query(Raca).all()
    
    for raca in racas:
        print(f"ID Raça: {raca.id_raca} | Classificação: {raca.classificacao}")

def deletar_raca(session):
    listar_racas(session)
    print()

    raca_id = int(input("Digite o ID da raça que deseja excluir: "))

    try:
        raca = session.query(Raca).filter(Raca.id_raca == raca_id).one()

        session.delete(raca)
        session.commit()
        print("Raça excluída com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao excluir a raça: {e}")

def editar_raca(session):
    listar_racas(session)
    print()
    raca_id = int(input("Digite o ID da raça que deseja editar: "))

    try:
        raca = session.query(Raca).filter(Raca.id_raca == raca_id).one()

        classificacao = input("Digite a nova classificação da raça: ")

        raca.classificacao = classificacao

        session.commit()
        print("Raça atualizada com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao editar a raça: {e}")


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
            deletar_especie(session)
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
