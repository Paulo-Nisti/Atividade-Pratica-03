# A fórmula para calcular a área de uma circunferência é: área = π ×raio2. Considerando para
# este problema que π = 3.14159265: 

# Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π. 

# Entrada: A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.
# Saída: Apresente a mensagem "A=" seguido pelo valor da variável area, conforme exemplo
# abaixo, com 4 casas após o ponto decimal.





# 1. Definição do valor de pi
pi = 3.14159265

# 2. Leitura do valor do raio com uma mensagem para o usuário
raio = float(input("Digite o valor do raio: "))

# 3. Cálculo da área da circunferência
area = pi * (raio * raio) # Outra forma de calcular o quadrado

# 4. Exibição do resultado formatado
print(f"A={area:.4f}")