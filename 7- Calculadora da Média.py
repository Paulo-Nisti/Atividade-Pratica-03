# Faça um programa que leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, 
# correspondente às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, 
# para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". 

# Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". 
# Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". 
# Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".

#  No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. 
# Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada.
# Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). 
# e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais) ou "Aluno reprovado.", 
# (caso a média tenha ficado 4.9 ou menos). 

# Para estes dois casos
# (aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem "Media
# final: " seguido da média final para esse aluno.

# Entrada: A entrada contém quatro números de ponto flutuante correspondentes às notas dos alunos.
# Saída: Todas as respostas devem ser apresentadas com uma casa decimal. 
# As mensagens devem ser impressas conforme a descrição do problema. 
# Não esqueça de imprimir o enter após o final de cada linha, caso contrário obterá "Presentation Error".


# 1. Leitura das quatro notas de uma única linha
N1, N2, N3, N4 = map(float, input().split())

# 2. Definição dos pesos e cálculo da média ponderada
peso1, peso2, peso3, peso4 = 2, 3, 4, 1
soma_pesos = peso1 + peso2 + peso3 + peso4  # Total de pesos é 10

media = (N1 * peso1 + N2 * peso2 + N3 * peso3 + N4 * peso4) / soma_pesos

# 3. Exibição da média inicial (sempre acontece)
# O formato :.1f garante a exibição com uma casa decimal
print(f"Media: {media:.1f}")

# 4. Verificação do status do aluno
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:  # O aluno está em exame (média entre 5.0 e 6.9)
    print("Aluno em exame.")
    
    # 4.1. Leitura da nota do exame
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    
    # 4.2. Recálculo da média final
    media_final = (media + nota_exame) / 2
    
    # 4.3. Verificação do status final
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    # 4.4. Exibição da média final
    print(f"Media final: {media_final:.1f}")