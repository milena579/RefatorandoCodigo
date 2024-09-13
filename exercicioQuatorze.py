#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/tabuadaqualquernum.c

def Tabuada():
    numero = int(input('Informe um numero: '))
    
    if numero <= 0: 
        print('Não existe tabuada com este numero!')
    
    while numero > 0:
        print('\nT A B U A D A')
      
        for i in range (1, 11):
            print(f'{numero} x {i} = {numero*i}')
            
        
        numero = int(input('Informe um numero: '))
        
                
Tabuada()