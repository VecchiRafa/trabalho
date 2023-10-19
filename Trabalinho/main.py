import sys
from models import tabelas

def redirecionar_opcao(opcao):
    if opcao == "1":
        tabelas.executar()
    elif opcao == "2":
        print("Encerrando o programa.")
        sys.exit(0)  # Sair do programa
    else:
        print("Opção inválida. Tente novamente.")

def main():
    while True:
        print("\nOpções:")
        print("1. tabelas")
        print("2. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "2":
            print("Encerrando o programa.")
            break
        else:
            redirecionar_opcao(escolha)

if __name__ == "__main__":
    main()
