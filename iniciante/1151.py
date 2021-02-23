numbers = 3
fibonacci = [0,1]
a = 0
b = 1
c = 0
qtd = int(input())
if qtd == 1:
    print(0)
elif qtd == 2:
    print('%i %i'%(0,1))
else:
    while numbers <= qtd:
        c = a+b
        fibonacci.append(c)
        a = b
        b = c
        numbers += 1
    print(*fibonacci)
    
