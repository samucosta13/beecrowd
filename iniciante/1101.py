while True:
  M, N = [int(o) for o in input().split()]
  if M == 0 or N == 0:
    break
  else:
    if N > M:
      N, M = M, N
    
    #USANDO MATRIZ

    #soma = 0
    #lista = []
    #for s in range(N,M+1):
    #  soma = soma+s
    #  lista.append(s)
    #print(lista)
    #print(soma)

    #USANDO STRING

    lista = ''
    soma = 0
    for s in range(N,M+1):
      lista = lista+str(s)+' '
      soma = soma+s
    print(lista+'Sum=%i'%soma)
