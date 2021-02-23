soma = 0
A = int(input())
N = int(input())
while N <= 0:
    N = int(input())
i = 0
while i < N:
    soma = soma + i + A
    i += 1
print(soma)
