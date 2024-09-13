#https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/exer6vetor.c
import numpy as np

num = []

for i in range (0,10):
    num.append(int(input(f'Informe o {i+1} numero: ')))
    
for i in range (0,10):
    print(f'{i+1}° numero: {num[i]}')