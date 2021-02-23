X = int(input())
seq = []
while X != 0:
    for n in range(1,X+1):
        seq.append(n)
    print(*seq)
    seq = []
    X = int(input())
