N = int(input())
linha = 1
a = 1
b = a+1
c = b+1
while linha <= N:      
    print('%i %i %i PUM'%(a,b,c))
    a = c+2
    b = a+1
    c = b+1
    linha += 1
