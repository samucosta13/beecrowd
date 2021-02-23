i = 0
j = i + 1

contador = 1
vez = contador

while contador <= 33:
    if i == 0 or i == 1 or i == 2:
        print("I=%i J=%i"%(i,j))
    elif 1.8 < i <= 2 and vez == 1:
        i = 2
        j = i + 1
        print("I=%i J=%i"%(i,j))
    else:
        i = float(i)
        j = float(j)
        print("I=%.1f J=%.1f"%(i,j))        

    if vez < 3:
        j += 1
        vez += 1
    else:
        i += 0.2
        j = i + 1
        
        vez = 1
    contador += 1
