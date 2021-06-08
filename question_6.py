#Escreva um programa em Python que leia diversas frases até a palavra “Sair” ser digitada. Indique quais frases apresentam a palavra “eu”. (código)
datas = []
phrase = ''

while phrase != "Sair": 
    phrase = input('Digite uma frase: ')
    if phrase == "Sair":        
        break
    else: 
        datas.append(phrase)        

def check_word(list_phrase: list):
    list_eu, check = [], []      
    for i in range(0, len(list_phrase)):
        check = str(list_phrase[i]).split()        
        for c in check:
            if c == "eu":                
                list_eu.append(list_phrase[i])
    print(f'Essa é a lista com todas as frases: {list_phrase}')
    print(f'Essa é a lista que contém as frases com a palavra EU: {list_eu}')
    
            
check_word(datas)