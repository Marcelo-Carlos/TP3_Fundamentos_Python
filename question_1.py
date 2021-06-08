#Crie uma lista vazia
list_numbers = []
#Adicione os elementos: 1, 2, 3, 4 e 5,  usando append()
for i in range(1, 6):
    list_numbers.append(i)
#Imprima a lista
print(list_numbers)
#Agora, remova os elementos 3 e 6 (não esqueça de checar se eles estão na lista)
for c in list_numbers:
    if 3 in list_numbers:
        list_numbers.remove(3) 
    elif 6 in list_numbers:
        list_numbers.remove(6)
#Imprima a lista modificada              
print(list_numbers)
#Imprima também o tamanho da lista usando a função len()
print('Tamanho da lista é:', len(list_numbers))
#Altere o valor do último elemento para 6 e imprima a lista modificada.
list_numbers.pop(-1)
list_numbers.append(6)
print(list_numbers)
    