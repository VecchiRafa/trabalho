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
            from . import Servico
            Servico.executar()
        elif escolha == "2":
            from . import Cliente
            Cliente.executar()
        elif escolha == "3":
            from . import Funcionario
            Funcionario.executar()
        elif escolha == "4":
            from . import Reserva
            Reserva.executar()
        elif escolha == "5":
            from . import Pet
            Pet.executar()
        elif escolha == "6":
            from . import Raca
            Raca.executar()
        elif escolha == "7":
            from . import Especie
            Especie.executar()
        elif escolha == "8":
            from . import Pessoa
            Pessoa.executar()
        elif escolha == "9":
            from . import Pagamento
            Pagamento.executar()
        elif escolha == "10":
            from . import Endereco
            Endereco.executar()
        elif escolha == "11":
            from . import Contato
            Contato.executar()
        elif escolha == "12":
            from . import Cobranca
            Cobranca.executar()
        elif escolha == "13":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar()