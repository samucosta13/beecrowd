idade = int(input())
qtd = 0
qtd = int(qtd)
soma = 0
while idade > 0:
    qtd += 1
    soma = soma + idade
    idade = int(input())
print('%.2f'%(soma/qtd))
