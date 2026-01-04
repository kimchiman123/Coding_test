import sys

input = sys.stdin.readline

numbers = list(map(int, input().split()))

total = 0

for i in range(len(numbers)):
    total += pow(numbers[i], 2)

print(total % 10)