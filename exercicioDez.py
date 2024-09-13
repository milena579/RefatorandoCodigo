#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/exer9funcoes.c

def soma(num1, num2):
    valor = num1 + num2  
    return valor

def somaAte():
    primeiro = int(input('Informe o primeiro numero: '))
    segundo = int(input('Informe o segundo numero: '))
    res = soma(primeiro, segundo)
    
    print(f'A soma entre esses numeros e: {res}')
somaAte()