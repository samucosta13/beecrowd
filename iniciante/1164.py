N = int(input())
c = 1
vetor = []
while c <= N:
    X = int(input())
    for i in range(1,X):
        if X%i == 0:
            vetor.append(i)
    if sum(vetor) == X:
        print("{0} eh perfeito".format(X))
    else:
        print("{0} nao eh perfeito".format(X))
    vetor.clear()
    c += 1