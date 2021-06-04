N, M = [int(e) for e in input().split()]
w = 1
p = [int(p) for p in input().split()]
for i in range(1,N):
    if (p[i] - p[i-1]) > M:
        print('N')
        break
    else:
        if (i == N-1):
            print('S')
        else:
            None
