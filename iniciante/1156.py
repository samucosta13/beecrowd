i = 1
n = 1
S = int(0)
while i <= 39:
    somar = i/n
    S = S + somar
    n = n*2
    i = i + 2
print('%.2f'%S)
