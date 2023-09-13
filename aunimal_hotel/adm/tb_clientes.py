def menu_clientes():
    while True:
        print("Menu Clientes:")
        # Adicione as opções específicas para o menu de clientes aqui
        print("1. Voltar ao Menu Tabelas")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            break
        else:
            print("Opção inválida. Tente novamente.")
