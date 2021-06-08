#Faça uma funçãoum programa em Python que simula um lançamento de dados. 
# Lance o dado 100 vezes e armazene os resultados em um vetor. 
# Depois, mostre quantas vezes cada valor foi conseguido. 
# Dica: use um vetor de contadores (1-6) e uma função do módulo 'random' de Python 
# para gerar números aleatórios, simulando os lançamentos dos dados. (código)

from random import randint

def play_dice():
    plays = []

    for i in range(0, 100):  
        random = (randint(1, 6))
        plays.append(random)
    return print(plays) 

play_dice()
