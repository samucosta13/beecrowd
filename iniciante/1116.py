N = int(input())
conta = 1
while conta <= N:
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    if Y == 0:
        print('divisao impossivel')
    else:
        print('%.1f'%(X/Y))
    conta = conta + 1

