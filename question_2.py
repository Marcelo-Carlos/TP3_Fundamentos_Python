#Escreva um programa em Python que leia um vetor de 5 números inteiros e mostre-os. (código)
def read_vector(vet):
    for i in vet:
        if i >= 0:
            print(i)

read_vector([1, 2, 6, 8, -7, 0])