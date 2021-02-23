X = int(input())
Y = int(input())
soma = 0
if X > Y:
    troca = Y
    Y = X
    X = troca
sam = X
while sam <= Y:
    if sam%13 != 0:
        soma = soma + sam
    sam += 1
print(soma)
