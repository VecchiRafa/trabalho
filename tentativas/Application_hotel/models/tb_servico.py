from services.conect_bd import Base, Session
from sqlalchemy import DECIMAL, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER

#=================================================================================================================================
# tabela serviço

class Servico(Base):
    __tablename__ = "servico"
    
    id_servico: Mapped[int] = mapped_column("id_servico", INTEGER,nullable=False, primary_key=True, autoincrement=True)
    valor_total: Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)
    descricao: Mapped[str] = mapped_column(VARCHAR(200), nullable=False)


#=================================================================================================================================
# Adicionar serviço


def adicionar_servico(session):
    while True:
        valor_total_input = input("\nDigite o valor total do serviço: ")
        try:
            valor_total = float(valor_total_input)
            if valor_total >= 0:
                break  # Valor válido, saia do loop
            else:
                print("\vO valor total não pode ser negativo. Digite novamente.")
        except ValueError:
            print("\nEntrada inválida. Certifique-se de inserir um número válido.")

    descricao = input("Digite a descrição do serviço: ")
    novo_servico = Servico(valor_total=valor_total, descricao=descricao)
    session.add(novo_servico)
    session.commit()
    print("Serviço criado com sucesso!")



#=====================================================================================================================================
# listar serviço

def listar_servico(session):
    servicos = session.query(Servico).all()
    for servico in servicos:
        print(f"ID: {servico.id_servico} | Valor Total: {servico.valor_total} | Descrição: {servico.descricao}")


#=====================================================================================================================================
# editar serviço

def editar_servico(session):
    print()
    listar_servico(session)
    servico_id = int(input("\nDigite o ID do serviço que deseja atualizar: "))
    novo_valor_total = float(input("Digite o novo valor total do serviço(0.0): "))
    nova_descricao = input("Digite a nova descrição do serviço: ")
    
    servico = session.query(Servico).filter(Servico.id_servico == servico_id).one()
    servico.valor_total = novo_valor_total
    servico.descricao = nova_descricao
    session.commit()
    print(f"Serviço com ID {servico_id} atualizado com sucesso!")

#=====================================================================================================================================
# excluir serviço

def excluir_servico(session):
    print()
    listar_servico(session)
    servico_id = int(input("\nDigite o ID do serviço que deseja deletar: "))
    
    servico = session.query(Servico).filter(Servico.id_servico == servico_id).one()
    session.delete(servico)
    session.commit()
    print(f"Serviço com ID {servico_id} deletado com sucesso!")


#=====================================================================================================================================
def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar serviço")
        print("2. Adicionar serviço")
        print("3. Editar serviço")
        print("4. Deletar serviço")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_servico(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_servico(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            editar_servico(session)
        elif escolha == "4":
            print()
            print(50 * "=")
            print()
            excluir_servico(session)
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
