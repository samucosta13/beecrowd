R = int(input())
G = int(input())
B = int(input())
samu = 1
v = (R//G)**2
samu = samu + v
a = ((G//B)**2)*v
samu = samu + a
print(samu)
