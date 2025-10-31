# Crie um programa que solicite a idade do usuário e classifique-o em uma das seguintes categorias:

# Criança (0-12 anos),
# Adolescente (13-17 anos),
# Adulto (18-59 anos)
# Idoso (60 anos ou mais).



# Loop para garantir que a entrada seja um número válido
while True:
    idade_str = input("Digite a sua idade: ")
    
    # Verifica se o que foi digitado contém apenas números
    if idade_str.isdigit():
        idade = int(idade_str) # Converte para inteiro
        break # Sai do loop se a conversão for bem-sucedida
    else:
        print("Entrada inválida. Por favor, digite apenas números.")

# Estrutura condicional para classificar a idade
if idade <= 12:
    categoria = "Criança"
elif idade <= 17:
    categoria = "Adolescente"
elif idade <= 59:
    categoria = "Adulto"
else: # Se não for nenhuma das anteriores, é 60 ou mais
    categoria = "Idoso"

# Exibe o resultado final
print(f"\nCom {idade} anos, sua categoria é: {categoria}.")