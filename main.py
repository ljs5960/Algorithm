N = int(input())
arr = []

for _ in range(N):
	arr.append(int(input()))

#  Selection Sort
for i in range(N):
	min = i
	for j in range(i+1, N):
		if arr[j] < arr[min]:
			min = j
	arr[min], arr[i] = arr[i], arr[min]

for i in arr:
	print(i)