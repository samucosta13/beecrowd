N = int(input())
if N == 1:
    print(N)
else:
    f = N-1
    while f >= 1:
        N = N * f
        f = f-1
    print(N)
