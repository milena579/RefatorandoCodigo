def calculaIdade(quantidade):
    total = 0
    for i in range (0,quantidade):
        idade = int(input(f'Informe a idada criança {i+1}: '))
        total = total + idade
        
    media = float(total/quantidade)
    print(f'O total das idades é {total} anos\n')
    print(f'A media de idade é: {media}')
    
calculaIdade(2)  