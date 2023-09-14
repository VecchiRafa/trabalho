def executar():
    while True:
        print(50*"=")
        print("")
        print("TELA ADM")
        print("")
        print("\nOpções:")
        print("1. Serviços")
        print("2. Clientes")
        print("3. Funcionario")
        print("4. Profissao")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            # Importe e execute o módulo correspondente aqui
            from . import tb_servico
            tb_servico.executar()
        elif escolha == "2":
            # Importe e execute o módulo correspondente aqui
            from . import tb_cliente
            tb_cliente.executar()
        elif escolha == "3":
            # Importe e execute o módulo correspondente aqui
            from . import tb_funcionario
            tb_funcionario.executar()
        elif escolha == "4":
            # Importe e execute o módulo correspondente aqui
            from . import tb_profissao
            tb_profissao.executar()
        
        elif escolha == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar()
