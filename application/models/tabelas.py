def executar():
    while True:
        print(50*"=")
        print("")
        print("TABELAS")
        print("")
        print("\nOpções:")
        print("1. Serviços")
        print("2. Clientes")
        print("3. Funcionario")
        print("4. Reserva")
        print("5. Pet")
        print("6. Raca")
        print("7. Especie")
        print("8. Pessoa")
        print("9. Pagamento")
        print("10. Endereço")
        print("11. Contato")
        print("12. Cobrança")
        print("13. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            # Importe e execute o módulo correspondente aqui
            from . import servico
            servico.executar()
        elif escolha == "2":
            from . import cliente
            cliente.executar()
        elif escolha == "3":
            from . import funcionario
            funcionario.executar()
        elif escolha == "4":
            from . import reserva
            reserva.executar()
        elif escolha == "5":
            from . import pet
            pet.executar()
        elif escolha == "6":
            from . import raca
            raca.executar()
        elif escolha == "7":
            from . import especie
            especie.executar()
        elif escolha == "8":
            from . import pessoa
            pessoa.executar()
        elif escolha == "9":
            from . import pagamento
            pagamento.executar()
        elif escolha == "10":
            from . import endereco
            endereco.executar()
        elif escolha == "11":
            from . import contato
            contato.executar()
        elif escolha == "12":
            from . import cobranca
            cobranca.executar()
        elif escolha == "13":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar()