i = 1
j = 1 + 6

contador = 1
vez = contador

while contador <= 15:
    print("I=%i J=%i"%(i,j))
    if vez < 3:
        j -= 1
        vez += 1
    else:
        i += 2
        j = i + 6
        vez = 1
    contador += 1
