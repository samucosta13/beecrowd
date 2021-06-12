R = int(input())
G = int(input())
B = int(input())
v = (R//G)**2
a = ((G//B)**2)*v
print(v+a+1)
