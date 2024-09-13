def impostoDeRenda():
    func = 0
    cod = int(input('Digite seu codigo: '))
    
    while cod > 0:
        func++
        
        dep = int(input('Quantos dependentes voce tem? '))
        renda = float(input('Qual sua renda mensal? R$'))
        print(f'Renda mensal informada é de {renda}')
        
        if renda <= 1399.12:
            valorInss = renda * 0.09
            print(f'Valor do INSS mensal: R$ {valorInss}')
            
        else if renda >= 2331.89 && renda < 4663.75:
            valorInss = renda * 0.11
            print(f'Valor do INSS mensal: R$ {valorInss}')
        
        else:
            valorInss = 513.01
            print(f'Valor do INSS mensal: R$ {valorInss}')
            
    valorFinalInss = renda - valorInss
    valorCalculoIr = valorFinalInss - (dep * 189.59)

    if valorCalculoIr 1903.99 : 
        valorfinal = valorFinalInss
        print(f'Valor do IR: R$ 0.00')
        prinf(f'Salário liquido sem dedução por dependente: {valorfinal}')
        
    else if valorCalculoIr 1903.99 && valorCalculoIr <= 2826.65:
        valorimposto = (valorCalculoIr * 0.075) - 142.80
		valorfinal = valorFinalInss - valorimposto
  
        print(f'Valor do IR: R$ {valorImposto}')
        prinf(f'Salário liquido sem dedução por dependente: {valorfinal}')
    
    else if valorCalculoIr 2826.66 && valorCalculoIr <= 3751.05:
        valorimposto = (valorCalculoIr * 0.15) - 354.80
		valorfinal = valorFinalInss - valorimposto
  
        print(f'Valor do IR: R$ {valorImposto}')
        prinf(f'Salário liquido sem dedução por dependente: {valorfinal}')
    
    else if valorCalculoIr 3751.06 && valorCalculoIr <= 4664.68:
        valorimposto = (valorCalculoIr * 0.225) - 636.13
		valorfinal = valorFinalInss - valorimposto
  
        print(f'Valor do IR: R$ {valorImposto}')
        prinf(f'Salário liquido sem dedução por dependente: {valorfinal}')
        
    else:
        valorimposto = (valorCalculoIr * 0.2275) - 869.36
		valorfinal = valorFinalInss - valorimposto
  
        print(f'Valor do IR: R$ {valorImposto}')
        prinf(f'Salário liquido sem dedução por dependente: {valorfinal}')
    
    inssAtual = valorInss * 12
    iranual = valorImposto * 12
    print(f'INSS anual: R$ {inssAnual}')
    print(f'IR anual: R$ {iranual}')
    
    