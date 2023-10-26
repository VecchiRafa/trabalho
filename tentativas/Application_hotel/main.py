from models import *
import sys
sys.path.append('Trabalinho/models')

def redirecionar_opcao(opcao):
    if opcao == "1":
        import models.menu_tbs as modulo
        modulo.executar()
    elif opcao == "4":
        print("Encerrando o programa.")
    else:
        print("Opção inválida. Tente novamente.")

def main():
    while True:
        print("\nOpções:")
        print("\n1. menu de operações")
        print("2. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "2":
            print("Encerrando o programa.")
            break
        else:
            redirecionar_opcao(escolha)

if __name__ == "__main__":
    main()
