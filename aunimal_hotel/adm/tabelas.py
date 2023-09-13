def executar():
    while True:
        print("\nOpções:")
        print("1. Serviços")
        print("2. Clientes")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            # Importe e execute o módulo correspondente aqui
            import tb_servico
            tb_servico.executar()
        elif escolha == "2":
            # Importe e execute o módulo correspondente aqui
            from . import tb_cliente_pessoa
            tb_cliente_pessoa.executar()
        elif escolha == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar()
