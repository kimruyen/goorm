# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
A = []
for i in range(N):
    B = input()
    A.append(B)
D = []
for i in A:
    C = []
    for j in i:
        if j.lower() in ['a', 'e', 'i', 'o', 'u']:
            C.append(j)
    if len(C) == 0:
        D.append('???')
    else:
        D.append(''.join(C))

for i in D:
    print(i)
