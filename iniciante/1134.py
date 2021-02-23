codigo = int(input())
alcool = 0
gasolina = 0
diesel = 0
while codigo != 4:
    while codigo > 4 or codigo < 1:
        codigo = int(input())
    else:
        if codigo == 1:
            alcool += 1
        elif codigo == 2:
            gasolina += 1
        elif codigo == 3:
            diesel += 1
        codigo = int(input())
print('MUITO OBRIGADO')
print('Alcool: %i'%alcool)
print('Gasolina: %i'%gasolina)
print('Diesel: %i'%diesel)
