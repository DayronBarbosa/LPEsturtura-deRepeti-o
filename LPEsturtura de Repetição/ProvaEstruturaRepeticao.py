def exibir_menu():
    """ Exibe o menu de opções para o usuário. """
    print("\nMenu:")
    print("1 - Inserir número")
    print("2 - Exibir resultados")
    print("0 - Encerrar")
               
def main():
    total_numeros = 0
    soma = 0

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1/2/3): ")
        
        if opcao == '1':
            numero = input("Digite um número: ")
        
            if numero.lstrip('-').isdigit():
                numero = int(numero)
            
                if numero == 0:
                    break
            
                total_numeros += 1
                soma += numero
            else:
                print("Por favor, digite um número válido.")
    
        elif opcao == '2':
            if total_numeros > 0:
                media = soma / total_numeros
                print(f"Quantidade de números digitados: {total_numeros}")
                print(f"Soma dos Números: {soma}")
                print(f"Média Aritmética: {media:.2f}")
            else:
                print("Nenhum número foi digitado.")
            
        if opcao == '0':
            print("Encerrando o programa...")
            break

if __name__ == "__main__":
    main()