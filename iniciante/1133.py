X = int(input())
Y = int(input())
if X > Y:
    troca = Y
    Y = X
    X = troca
sam = X+1
while sam < Y:
    if sam%5 == 2 or sam%5 == 3:
        print(sam)
    sam += 1
