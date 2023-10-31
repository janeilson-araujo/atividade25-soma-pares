# Exercício Python 25: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print("o programa lê seis números inteiros e mostra a soma apenas daqueles que forem pares")
numeros = []

for num in range(1 ,7):
    numero_usuario = int(input(f"insira o numero {num} :"))
    if numero_usuario % 2 == 0:
       numeros.append(numero_usuario)

soma = sum(numeros)
print(f"a soma dos numeros pares é: {soma}")