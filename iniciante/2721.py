r = [int (r) for r in input().split()]
renas = ['Rudolph','Dasher','Dancer','Prancer','Vixen','Comet','Cupid','Donner','Blitzen']
b = 0
for s in range(len(r)):
    b = b + r[s]
resto = b%9
for t in range(0,8):
    if resto == t:
        print(renas[t])
