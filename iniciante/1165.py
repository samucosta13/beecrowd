N = int(input())
vetor = []
for i in range(0,N):
    X = int(input())
    for d in range(1,X+1):
        if X%d == 0:
            vetor.append(d)
    if len(vetor) == 2:
        print("{0} eh primo".format(X))
    else:
        print("{0} nao eh primo".format(X))
    vetor.clear()