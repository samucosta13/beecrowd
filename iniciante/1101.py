sequencia = []
soma = 0

M, N = input().split()
M = int(M)
N = int(N)

while M > 0 and N > 0: 
    if M < N:
        for seq in range(M,N+1):
            soma = soma + seq
            sequencia.append(seq)
        print(*sequencia,'Sum=%i'%(soma))
        sequencia.clear()
        soma = 0

    elif M > N:
        for seq in range(N,M+1):
            soma = soma + seq
            sequencia.append(seq)
        print(*sequencia,'Sum=%i'%(soma))
        sequencia.clear()
        soma = 0

    #else:
        #soma = M
        #sequencia.append(N)
        #print(*sequencia,'Sum=%i'%(soma))
        #sequencia.clear()
        #soma = 0

    M, N = input().split()
    M = int(M)
    N = int(N)
