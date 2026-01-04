# 구간 합 구하기 4
import sys

input = sys.stdin.readline 

n, m = map(int, input().strip().split())

numbers = list(map(int, input().strip().split()))
sum_numbers = [0] * (len(numbers) + 1)
sum_numbers[1] = numbers[0]
for i in range(1, len(numbers)+1):
    sum_numbers[i] = sum_numbers[i-1] + numbers[i-1]

#print(sum_numbers)
for _ in range(m):
    a, b = map(int, input().strip().split())
    print(sum_numbers[b] - sum_numbers[a-1])
