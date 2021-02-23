X = int(input())
Z = int(input())
while Z <= X:
    Z = int(input())
numbers = 0
soma = 0
while soma <= Z:
    soma = soma + X
    numbers = numbers + 1
    X += 1
print(numbers)
