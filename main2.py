# 'if', 'and', 'else' e 'elif'.

salario = float(input('Digite o seu salário: '))

if salario <= 2500:
    print('Você é um desenvolvedor Junior!')
elif salario > 2500 and salario <= 4000:
    print('Você é um desenvolvedor Pleno!')
elif salario > 4000 and salario <= 15000:
    print('Você é um desenvolvedor Sênior!')
else:
    print('Você é um gerente de projetos!')     