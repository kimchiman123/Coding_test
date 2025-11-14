N = int(input())

total = 0
array = []
array = list(map(int, input().split()))

max_array = max(array)

for i in range(len(array)):
    total += array[i]/max_array * 100

print(total/N)
