# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/listalaco2.c

total = 0
for i in range (0, 10):
    salario = float(input(f'Informe o salario {i+1}:'))
    total = total + salario
    
media = total / 10
print(f'Total dos salarios: {total}\n')
print(f'Media dos salarios: {media}')