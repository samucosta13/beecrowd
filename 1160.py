T = int(input())
c = 1
while c <= T:
    PA, PB, G1, G2 = [str (s) for s in input().split()]
    PA = int(PA)
    PB = int(PB)
    if PA > PB:
        (PA, PB) = (PB, PA)
    G1 = float(G1)
    G2 = float(G2)
    if G2 > G1:
        (G1, G2) = (G2, G1)
    (G1, G2) = ((G1/100),(G2/100))
    anos = 0
    while PA <= PB:
        if anos > 100:
            print("Mais de 1 seculo.")
            break
        else:
            PA = round(PA + (PA*G1))
            PB = round(PB + (PB*G2))
            anos += 1
        if PA > PB:
            print("{0} anos.".format(anos))
    c += 1