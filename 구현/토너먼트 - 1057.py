N = int(input())

array = list(map(int, input().split()))
array.sort(reverse=False)

time = 0
sum = 0

for i in range(N):
    sum += array[i]
    time += sum
print(time)
