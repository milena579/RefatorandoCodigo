#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/EX_04.c
def conta(num):
    if( num <= 100):
        print(f'{num}')
        conta(num + 1)
        
num = int(input('Digite um numero para ir dele ate 100: '))
conta(num)
    