N, M = input().split()
N = int(N)
M = int(M)
sobrou = N
w = 0
pa = []
ca = []
def funcao(N,M,w,pa,ca,sobrou):
    while True:
        print('Paula =',pa[w])
        print('resto =',sobrou)
        
        if sobrou > M and pa[w] != M:
            ca.insert(w,M)
            sobrou = sobrou - M
        elif sobrou > M and pa[w] == M:
            ca.insert(w,M-1)
            sobrou = sobrou - M + 1
        elif sobrou == M and pa[w] != M:
            print('Carlos')
            break
        elif 0 < sobrou < M:
            if pa[w] != sobrou:
                print('Carlos')
                break
            elif (sobrou - 1) > 0:
                ca.insert(w,sobrou-1)
                sobrou = 1
            else:
                print('Paula')
                break
        print('Carlos =',ca[w])
        print('resto =',sobrou)
        w += 1
        if sobrou > M and ca[w-1] != M:
            pa.insert(w,M)
            sobrou = sobrou - M
        elif sobrou > M and ca[w-1] == M:
            pa.insert(w,M-1)
            sobrou = sobrou - M + 1
        elif sobrou == M and ca[w-1] != M:
            print('Paula')
            break
        elif 0 < sobrou < M:
            if ca[w-1] != sobrou:
                print('Paula')
                break
            elif (sobrou - 1) > 0:
                pa.insert(w,sobrou-1)
                sobrou = 1
            else:
                print('Carlos')
                break
if sobrou > M:
    pa.insert(0,M)
    sobrou = sobrou - M
    funcao(N,M,w,pa,ca,sobrou)
else:
    pa.insert(0,N)
    print('Paula')

