# Exercício Python 25: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o
variavel1= 0
for i in range(1, 7):
    numero = int(input(f'digite o {i}° numero:'))
    if numero % 2 == 0:
        variavel1 += numero
    print(f'a soma do numero é:{variavel1}')