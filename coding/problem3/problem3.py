# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from datetime import datetime

user_input = int(input())
x = []

for i in range(user_input):
    a, b = input().split()
    s1, s2 = a.split('/')
    e1, e2 = b.split('/')
    start = int(s1) * 100 + int(s2)
    end = int(e1) * 100 + int(e2)
    x.append([start, end])

y = sorted(x, key=lambda data: (data[0], -data[1]))

h = 1
item = []

for i in y:
    item.append([i[0], h])
    item.append([i[1], -h])
    h += 1
item = sorted(item)


def func(data):
    z = []
    for i in data:
        if i[1] > 0:
            z.append(i)
        else:
            if z[-1][1] == abs(i[1]):
                z.pop()
            else:
                return "No"
    return "Yes"


print(func(item))
