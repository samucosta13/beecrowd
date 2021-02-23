nota1 = float(input())
while nota1 > 10 or nota1 < 0:
    print('nota invalida')
    nota1 = float(input())
nota2 = float(input())
while nota2 > 10 or nota2 < 0:
    print('nota invalida')
    nota2 = float(input())
media = (nota1+nota2)/2
print('media = %.2f'%media)
