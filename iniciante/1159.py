X = int(input())
while X != 0:
    par = int(0)
    soma = int(0)
    while par < 5:
        if X%2 == 0:
            soma = soma + X
            par = par + 1
        X = X + 1
    print(soma)
    X = int(input())
