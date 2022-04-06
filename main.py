N = int(input())
arr = []

for i in range(N):
	i, j = input().split(' ')
	arr.append(int(i))
	arr.append(int(j))

for i in arr:
	print(i, end=' ')