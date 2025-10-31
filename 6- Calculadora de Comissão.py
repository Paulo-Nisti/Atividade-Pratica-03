# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas
# efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
# sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais. 

# Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de
# dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e
# montante total das vendas efetuadas por este vendedor, respectivamente. 

# Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.


# 1. Leitura dos dados com mensagens para o usuário
nome_vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: R$ "))
total_vendas = float(input("Digite o total de vendas no mês: R$ "))

# 2. Cálculo da comissão de 15%
# 15% é o mesmo que multiplicar por 15/100 ou 0.15
comissao = total_vendas * 0.15

# 3. Soma do salário fixo com a comissão
salario_final = salario_fixo + comissao

# 4. Impressão do resultado final no formato especificado
print("\n--- Folha de Pagamento ---")
print(f"Vendedor: {nome_vendedor}")
print(f"TOTAL = R$ {salario_final:.2f}")