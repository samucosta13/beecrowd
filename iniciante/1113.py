X, Y = input().split()
X = int(X)
Y = int(Y)
while X != Y:
    if X > Y:
        print('Decrescente')
    else:
        print('Crescente')
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
