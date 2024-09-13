def somaSempre(valorUm, valorDois):
    if(valorDois == 1):
        return valorUm
    else:
        return valorUm + somaSempre(valorUm, valorDois - 1)

num1 = int(input('Informe o primeiro numero: '))
numVezes = int(input('Informe o numero de vezes que o 1° numero sera somado: '))

resp = somaSempre(num1, numVezes)

print(f'Resposta: {resp}')