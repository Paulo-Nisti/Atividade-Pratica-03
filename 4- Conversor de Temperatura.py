# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.


# --- Conversor de Temperaturas - Versão Completa ---

def obter_temperatura():
    """Solicita e valida o valor numérico da temperatura."""
    while True:
        valor_str = input("Digite o valor da temperatura: ").replace(',', '.')
        try:
            return float(valor_str)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def obter_unidade(mensagem):
    """Solicita e valida a unidade de temperatura (C, F ou K)."""
    while True:
        unidade = input(mensagem).strip().upper()
        if unidade in ['C', 'F', 'K']:
            return unidade
        # Permite que o usuário digite o nome completo
        elif unidade in ["CELSIUS", "FAHRENHEIT", "KELVIN"]:
            return unidade[0] # Retorna apenas a primeira letra
        else:
            print("Unidade inválida. Por favor, escolha C, F ou K.")

def converter_temperatura(valor, origem, destino):
    """Realiza a conversão da temperatura."""
    # Se as unidades forem iguais, não há o que converter
    if origem == destino:
        return valor

    # Passo 1: Converter a temperatura de entrada para Celsius (nossa base)
    temp_em_celsius = 0
    if origem == 'F':
        temp_em_celsius = (valor - 32) * 5 / 9
    elif origem == 'K':
        temp_em_celsius = valor - 273.15
    else: # origem == 'C'
        temp_em_celsius = valor

    # Passo 2: Converter de Celsius para a unidade de destino
    resultado_final = 0
    if destino == 'F':
        resultado_final = (temp_em_celsius * 9 / 5) + 32
    elif destino == 'K':
        resultado_final = temp_em_celsius + 273.15
    else: # destino == 'C'
        resultado_final = temp_em_celsius
        
    return resultado_final

# --- Bloco Principal do Programa ---
print("--- Conversor Universal de Temperaturas ---")
temperatura_inicial = obter_temperatura()
unidade_origem = obter_unidade("Qual a unidade de origem (C, F, K)? ")
unidade_destino = obter_unidade("Para qual unidade deseja converter (C, F, K)? ")

# Realiza o cálculo
temperatura_convertida = converter_temperatura(temperatura_inicial, unidade_origem, unidade_destino)

# Formata os símbolos para uma exibição elegante
simbolo_origem = "K" if unidade_origem == 'K' else f"°{unidade_origem}"
simbolo_destino = "K" if unidade_destino == 'K' else f"°{unidade_destino}"

# Exibe o resultado final
print("\n--- Resultado da Conversão ---")
print(f"{temperatura_inicial:.2f} {simbolo_origem} é igual a {temperatura_convertida:.2f} {simbolo_destino}")