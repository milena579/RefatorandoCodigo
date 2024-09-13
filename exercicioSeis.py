def procuraNum():
    val = [10]
    
    for i in range (0, 10):
        numero = int(input(f'Informe o valor {i+1}: '))
        val.append(numero)
        
    busca = int(input('Informe um valor a ser procurado: '))
    
    achou = 0
    for i in range (0, 10):
        if busca == val[i+1]:
            achou = achou + 1
    
    print(f'O numero foi achado {achou} vezes')
procuraNum()