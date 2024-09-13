#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/EX_02.c

def calculaPI(valor):
    if id(valor) %2 == 0:
        pi = 'P'
        return(pi)
    else:
        pi = 'I'
        return(pi)
    
def calculadoraSimples():
    primeiroNum = int(input('Digite o primeiro numero: '))
    segundoNum = int(input('Digite o segundo numero: '))

    soma =  primeiroNum + segundoNum
    multi = primeiroNum * segundoNum
    
    print(f'A soma dos numeros eh {soma} \nA multiplicacao dos numeros eh {multi}')
    calculaPI(soma)

calculadoraSimples()