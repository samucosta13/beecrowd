grenais = 0
vit_inter = 0
vit_gremio = 0
empates = 0
inter, gremio = input().split()
inter = int(inter)
gremio = int(gremio)
grenais += 1
if inter > gremio:
    vit_inter += 1
elif gremio > inter:
    vit_gremio += 1
else:
    empates += 1
print('Novo grenal (1-sim 2-nao)')
grenal = int(input())
while grenal == 1:
    grenais += 1
    inter, gremio = input().split()
    inter = int(inter)
    gremio = int(gremio)
    
    if inter > gremio:
        vit_inter += 1
    elif gremio > inter:
        vit_gremio += 1
    else:
        empates += 1
    print('Novo grenal (1-sim 2-nao)')
    grenal = int(input())
else:
    print('%i grenais'%grenais)
    print('Inter:%i'%vit_inter)
    print('Gremio:%i'%vit_gremio)
    print('Empates:%i'%empates)
    if vit_inter > vit_gremio:
        print('Inter venceu mais')
    elif vit_gremio > vit_inter:
        print('Gremio venceu mais')
    else:
        print('Nao houve vencedor')
