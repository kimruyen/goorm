# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
a, b = input().split(' ')
def x(a, b):
	if a != b or a == 1 or b == 1:
		return 2
	else:
		for i in range(2, a+1):
			if a % i == 0:
				return i
	
print(x(int(a), int(b)))
