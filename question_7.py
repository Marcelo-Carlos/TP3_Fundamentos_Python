#Escreva um programa em Python que realiza operações de inclusão e remoção em listas. 
# Seu programa deve perguntar ao usuário qual operação deseja fazer:
#Mostrar lista;Incluir elemento;
#Remover elemento;
#Apagar todos os elementos da lista.

list_operation = ['casa', 'carro', 29, 30, 'maria']
operation = ''


while operation != 'X':  
    print("======================================")
    print('OPERAÇÕES DISPONÍVEIS')
    print('A - Mostrar o conteúdo da lista')
    print('B - Incluir elemento')
    print('C - Remover elemento')
    print('D - Apagar todos os elementos da lista')
    print('X - Sair')
    print("======================================")
    operation = input('Qual operação deseja fazer? ')
    print("======================================")
    
    if operation == 'A':
        print(list_operation)
        
    elif operation == 'B':
        new = input('Digite novo elemento: ')
        list_operation.append(new)
        
    elif operation == 'C':
        delete = input('Digite o elemento que queira remover: ')    
        if delete in list_operation:
            list_operation.remove(delete)
        else:
            print('Elemento não exite')
            
    elif operation == 'D':
        list_operation.clear()
        print('Lista vazia')        
    
    elif operation == 'X':
        print('Operação encerrada')        
        break       
    
        
   


    