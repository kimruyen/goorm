A = input()
B = A

A = A.replace('12', '전', 1)
A = A.replace('21', '후', 1)
B = B.replace('21', '전', 1)
B = B.replace('12', '후', 1)

if '전' in A+B and '후' in A+B:
	print('Yes')
else:
	print('No')