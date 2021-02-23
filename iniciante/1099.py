N = int(input())

soma = 0

c = 1
while c <= N:
    X, Y = input().split()
    X = int(X)
    Y = int(Y)

    if X > Y:
        for impar in range(Y+1,X):
            if impar%2 != 0:
                soma = soma + impar
        print(soma)

    else:
        for impar in range(X+1,Y):
            if impar%2 != 0:
                soma = soma + impar
        print(soma)

    soma = 0

    c += 1
