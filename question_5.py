#Escreva um programa em Python que leia nomes de alunos e suas alturas em metros até que um nome de aluno seja o código de saída “Sair”. 
# O programa deve possuir uma função que indica todos os alunos que tenham altura acima da média (a média aritmética das alturas de todos os alunos lidos). (código)
datas = {}
height = 0
name = ''

while name != "Sair": 
    name = input('Nome do aluno: ')    
    if name == "Sair":        
        break
    else:           
        height = float(input('Altura do aluno: '))
        datas.setdefault(name, height)       

    
def avg_heigth(list_dic: dict):
    calc, avg = 0, 0
    lis_avg = {}
    for k, v in list_dic.items():
        calc += v
        avg = calc / len(list_dic)   
    for k, v in list_dic.items():
        if v > avg:
            lis_avg.setdefault(k, v)
    print(f'Média de altura: {avg}.')
    if len(lis_avg) > 0:
        print(f'Segue lista de alunos acima da média: {lis_avg}')
    else:
        print('Nenhum aluno acima da média')
    
avg_heigth(datas)
    