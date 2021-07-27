N, M = [int(u) for u in input().split()]
me = []
for mem in range(1,N+1):
    me.append(int(mem))
w = 1
print(me)
while w <= M:
    i, X, Y = [str(s) for s in input().split()]
    X = int(X) -1
    Y = int(Y) -1
    if i == 'S':
        soma = 0
        if X > Y:
            xy = X
            X = Y
            Y = xy          
        for sp in range(X,Y+1):
            soma = soma+me[sp]
        print(soma)
    elif i == 'I':
        while X< Y:
            me.insert(Y,me[X])
            yy = me[Y+1]
            me.remove(Y+1)
            me.insert(X,yy)
            me.remove(X+1)
            X = X+1
            Y = Y-1
            
    w = w+1
