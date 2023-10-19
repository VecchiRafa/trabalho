import sys

def redirecionar_opcao(opcao):
    if opcao == "1":
        import modles.tabelas as modulo
        modulo.executar()
    elif opcao == "4":
        print("Encerrando o programa.")
    else:
        print("Opção inválida. Tente novamente.")

def main():
    while True:
        print("\nOpções:")
        print("1. Adm")
        print("2. Funcionário")
        print("3. Cliente")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "8":
            print("Encerrando o programa.")
            break
        else:
            redirecionar_opcao(escolha)
        
if __name__ == "__main__":
    main()
