def conta(num):
    if( num <= 100):
        print(f'{num}')
        conta(num + 1)
        
num = int(input('Digite um numero para ir dele ate 100: '))
conta(num)
    