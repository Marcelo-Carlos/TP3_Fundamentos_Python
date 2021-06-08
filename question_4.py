#Escreva um programa em Python que leia um vetor de números de tamanho t. Leia t previamente. Em seguida, faça seu programa verificar quantos números iguais a 0 existem nele. (código)
def read_numbers(numbers: list):   
    equal_numbers = []
    for i in numbers:
        if i not in equal_numbers:
            equal_numbers.append(i)
    print(f'{len(equal_numbers)} números repetidos. São: {equal_numbers}')

read_numbers([1, 2, 5, 2, 1, 3, 5, 3])