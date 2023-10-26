# 

from tb_funcionario import Funcionario, listar_funcionario
from sqlalchemy import DATETIME, ForeignKey, DECIMAL, DATE
from sqlalchemy.orm import Mapped, mapped_column 
from sqlalchemy.dialects.mysql import INTEGER
from datetime import datetime, date
from services.conect_bd import Base, Session

class Pagamento(Base):
    __tablename__ = "pagamento"
    
    valor: Mapped[float] = mapped_column(DECIMAL(10,2), nullable=False)
    data_pagamento: Mapped[datetime] = mapped_column(DATETIME, nullable=False, default=datetime.now())
    mes_referencia: Mapped[date] = mapped_column(DATE, nullable=False, primary_key=True)
    id_funcionario: Mapped[int] = mapped_column("id_funcionario", INTEGER, ForeignKey(Funcionario.id_funcionario), primary_key=True, nullable=False)  


# Função para adicionar um pagamento
def adicionar_pagamento(session):
    valor = float(input("Digite o valor do pagamento: "))
    mes_referencia = date.fromisoformat(input("Digite o mês de referência (AAAA-MM-DD): "))
    print()
    listar_funcionario(session)
    print()
    id_funcionario = int(input("Digite o ID do funcionário: "))

    novo_pagamento = Pagamento(valor=valor, data_pagamento=datetime.now(), mes_referencia=mes_referencia, id_funcionario=id_funcionario)
    session.add(novo_pagamento)
    session.commit()
    print("Pagamento adicionado com sucesso!")

# Função para listar todos os pagamentos
def listar_pagamentos(session):
    pagamentos = session.query(Pagamento).all()
    for pagamento in pagamentos:
        print(f"ID Funcionário: {pagamento.id_funcionario} | Valor: {pagamento.valor} | Mês de Referência: {pagamento.mes_referencia}")

# Função para atualizar informações de um pagamento
def atualizar_pagamento(session):
    mes_referencia = date.fromisoformat(input("Digite o mês de referência do pagamento que deseja atualizar (AAAA-MM-DD): "))

    listar_funcionario(session)
    print()
    id_funcionario = int(input("Digite o ID do funcionário associado ao pagamento: "))
    
    pagamento = session.query(Pagamento).filter_by(mes_referencia=mes_referencia, id_funcionario=id_funcionario).first()
    
    if pagamento:
        novo_valor = float(input("Digite o novo valor do pagamento: "))
        pagamento.valor = novo_valor
        session.commit()
        print("Informações do pagamento atualizadas com sucesso.")
    else:
        print("Pagamento não encontrado.")

# Função para excluir um pagamento
def excluir_pagamento(session):
    listar_pagamentos(session)
    mes_referencia = date.fromisoformat(input("Digite o mês de referência do pagamento que deseja excluir (AAAA-MM-DD): "))
    id_funcionario = int(input("Digite o ID do funcionário associado ao pagamento: "))
    
    pagamento = session.query(Pagamento).filter_by(mes_referencia=mes_referencia, id_funcionario=id_funcionario).first()
    
    if pagamento:
        session.delete(pagamento)
        session.commit()
        print("Pagamento excluído com sucesso.")
    else:
        print("Pagamento não encontrado.")

def executar():
    # Iniciar uma sessão
    session = Session()

    while True:
        print()
        print(50 * "=")
        print()
        print("\nOpções:")
        print("1. Listar pagamentos")
        print("2. Adicionar pagamento")
        print("3. Editar pagamento")
        print("4. Deletar pagamento")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print()
            print(50 * "=")
            print()
            listar_pagamentos(session)
        elif escolha == "2":
            print()
            print(50 * "=")
            print()
            adicionar_pagamento(session)
        elif escolha == "3":
            print()
            print(50 * "=")
            print()
            atualizar_pagamento(session)
        elif escolha == "4":
            print()
            print(50 * "=")
            print()
            excluir_pagamento(session)
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
