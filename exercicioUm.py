# https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/listacondicional3.c

def calcularSalario():
    salarioMinimo = 1412
    salarioBruto = float(input('Informe seu salario BRUTO: '))
    desc = float(input('Informe o DESCONTO a ser aplicado pensano em porcentagem: '))
    
    desc = ((salarioBruto * desc) / 100)
    salarioLiquido = salarioBruto - desc
    
    if desc < salarioMinimo:
        print(f'O salario liquido é {salarioLiquido}, e seus impostos estão MENORES que um salario mínimo')
    else:
        print(f'O salario liquido é {salarioLiquido}, e seus impostos estão MAIORES que um salario mínimo')
        
        
calcularSalario()