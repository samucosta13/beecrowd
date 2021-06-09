N = int(input())
w = 1
raio = []
sam = True
while w <= N:
    X, Y = [int(xy) for xy in input().split()]
    raio.append([X,Y])
    w += 1
for s in range(len(raio)):
    for i in range(len(raio)):
        if raio[s][0] == raio[i][0] and raio[s][1] == raio[i][1] and s != i:
            sam = False
            break
if sam is False:
    print(1)
else:
    print(0)
