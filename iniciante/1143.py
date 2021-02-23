N = int(input())
linha = 1
a = 1
b = a**2
c = a**3
while linha <= N:      
    print('%i %i %i'%(a,b,c))
    print('%i %i %i'%(a,b+1,c+1))
    a += 1
    b = a**2
    c = a**3
    linha += 1
