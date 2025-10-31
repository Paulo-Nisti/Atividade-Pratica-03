# Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
# O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
# calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.


# < 18.5: classificacao = "Abaixo do peso" 
# < 25: classificacao = "Peso normal"
# < 30: classificacao = "Sobrepeso"
# Para os demais cenários: classificacao = "Obeso"


# --- Calculadora de IMC com Classificação ---

def obter_valor(mensagem):
    """Função para solicitar e validar a entrada do usuário (peso ou altura)."""
    while True:
        valor_str = input(mensagem)
        # Permite vírgula e ponto como separador decimal
        valor_str = valor_str.replace(',', '.')
        try:
            # Tenta converter o valor para float
            valor = float(valor_str)
            if valor > 0:
                return valor
            else:
                print("Valor inválido. Por favor, digite um número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# 1. Solicita o peso e a altura ao usuário
print("--- Calculadora de Índice de Massa Corporal (IMC) ---")
peso = obter_valor("Digite seu peso em kg (ex: 70.5): ")
altura = obter_valor("Digite sua altura em metros (ex: 1.75): ")

# 2. Calcula o IMC
# A operação ** 2 eleva a altura ao quadrado
imc = peso / (altura ** 2)

# 3. Classifica o resultado do IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

# 4. Exibe o resultado completo
print("\n--- Resultado ---")
# O formato :.2f arredonda o IMC para duas casas decimais
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")