def executar():
    while True:
        print(50*"=")
        print("")
        print("TELA ADM")
        print("")
        print("\nOpções:")
        print("1. Pessoas")
        print("2. Clientes")
        print("3. Funcionario")
        print("4. Profissao")
        print("5. pet")
        print("6. raca")
        print("7. especie")
        print("8. endereço")
        print("9. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            # Importe e execute o módulo correspondente aqui
            from . import tb_pessoa
            tb_pessoa.executar()
        elif escolha == "2":
            # Importe e execute o módulo correspondente aqui
            from . import tb_cliente
            tb_cliente.executar()
      
        elif escolha == "7":
            # Importe e execute o módulo correspondente aqui
            from . import tb_especie
            tb_especie.executar()
        elif escolha == "8":
            # Importe e execute o módulo correspondente aqui
            from . import tb_endereco
            tb_endereco.executar()
        
        elif escolha == "9":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar()
