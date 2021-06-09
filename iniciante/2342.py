N = int(input())
P, C, Q = input().split()
P = int(P)
Q = int(Q)
if C == '+':
    if (P + Q) <= N:
        print('OK')
    else:
        print('OVERFLOW')
elif C == '*':
    if (P * Q) <= N:
        print('OK')
    else:
        print('OVERFLOW')
