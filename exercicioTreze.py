#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/trabalho_moldularizacao.c

def calculo(n1, n2, n3, n4):
    resp = (n1 + n2 + n3 + n4) / 4
    return resp

def mostra(nome = [], mat = 0, media = 0):
    
    print(f'O aluno {nome} com matricula {mat} tem media {media}')
        
        

def notas():
    matricula = 0
    matricula = int(input('Informe sua matricula: '))
    
    while matricula != 0:
        nome = [] 
        nome.append(str(input('Informe seu nome: ')))
        n1 = float(input('Informe sua PRIMEIRA nota: '))
        n2 = float(input('Informe sua SEGUNDA nota: '))
        n3 = float(input('Informe sua TERCEIRA nota: '))
        n4 = float(input('Informe sua QUARTA nota: '))
        
        media = calculo(n1,n2,n3,n4)
        mostra(nome, matricula, media)

        matricula = int(input('Informe sua matricula: '))
notas()
        
        
