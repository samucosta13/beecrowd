N, K = input().split()
N = int(N)
K = int(K)
bala = [int(bala) for bala in input().split()]
tipo = []
cada = []
for a in range(K):
    tipo.insert(a,a+1)
    cada.insert(a,0)
for i in range(N):
    for j in range(K):
        if bala[i] == tipo[j]:
            cada[j] += 1
print(min(cada))
