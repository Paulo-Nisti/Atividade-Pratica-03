# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.


# --- Verificador de Ano Bissexto (Versão Robusta) ---

def eh_bissexto(ano):
    """
    Função que recebe um ano e retorna True se for bissexto,
    e False caso contrário.
    """
    # A lógica pode ser escrita de forma mais compacta:
    # Um ano é bissexto se (é divisível por 4 E não por 100) OU (é divisível por 400).
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# Loop para garantir que a entrada seja um número válido
while True:
    ano_str = input("Digite um ano para verificar: ")
    if ano_str.isdigit():
        ano_int = int(ano_str)
        if ano_int > 0:
            break  # Sai do loop se a entrada for um ano válido
        else:
            print("Por favor, digite um ano maior que zero.")
    else:
        print("Entrada inválida. Por favor, digite apenas números.")

# Chama a função para verificar e exibe o resultado
if eh_bissexto(ano_int):
    print(f"\nSim, o ano {ano_int} é bissexto.")
else:
    print(f"\nNão, o ano {ano_int} não é um ano bissexto.")

