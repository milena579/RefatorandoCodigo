#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/exer19funcoes.c

def IMC():
    sexo = str(input('Informe seu sexo((M) Masculino e (F) Feminino): ')).upper()
    
    altura = float(input('Informe sua altura (com (.) separando metros de centimetros):\n'))
    
    if(sexo == 'M'):
        resul = round((72.7 * altura) - 58)
        print(f'Seu peso ideal eh: {resul}KG')
    else:
        resul = round((62.1 * altura) - 44.7)
        print(f'Seu peso ideal eh: {resul}KG')
        

IMC()