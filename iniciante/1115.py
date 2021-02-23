X, Y = input().split()
X = int(X)
Y = int(Y)
while X != 0 and Y != 0:
    if X > 0 and Y > 0:
        print('primeiro')
    elif X < 0 and Y > 0:
        print('segundo')
    elif X < 0 and Y < 0:
        print('terceiro')
    elif X > 0 and Y < 0:
        print('quarto')
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
