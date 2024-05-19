#Calculadora de Média:
#Crie um programa que calcule a média de um conjunto de notas fornecidas pelo usuário utilizando um laço de repetição for para iterar sobre as notas.

# Solicita ao usuário a quantidade de notas que serão inseridas
num_notas = int(input("Quantas notas deseja inserir? "))

# Inicializa a variável para armazenar a soma das notas
soma = 0

# Utiliza um laço de repetição for para iterar sobre as notas e calcular a soma
for i in range(num_notas):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma += nota

# Calcula a média das notas
media = soma / num_notas

# Imprime a média das notas na saída padrão
print(f"A média das {num_notas} notas é: {media:.2f}")

#Este código solicita ao usuário a quantidade de notas que serão inseridas, depois itera sobre as notas utilizando um laço de repetição for, calculando a soma total das notas. Em seguida, calcula a média das notas dividindo a soma pelo número de notas fornecidas e imprime o resultado na saída padrão.

