# lado da etiqueta vermelha
R = int(input())
# lado da(s) etiqueta(s) verdes
G = int(input())
# lado da(s) etiqueta(s) azuis
B = int(input())

#samu = total de etiquetas (começa com 1 etiqueta grandona vermelha sempre)
samu = 1
v = (R//G)**2
samu = samu + v
a = ((G//B)**2)*v
samu = samu + a

# saída do total final
print(samu)

# tira print :)
