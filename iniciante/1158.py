N = int(input())
c = int(0)
while c < N:
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    soma = int(0)
    impar = int(1)
    while impar <= Y:
        if X%2 != 0:
            soma = soma + X
            impar += 1
        X += 1
    print(soma)
    c += 1
