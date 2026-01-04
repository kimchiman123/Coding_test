# 수 정렬하기 2
import sys

input = sys.stdin.readline 

n = int(input())

numbers = []

for _ in range(n):
    numbers.append(int(input()))

numbers.sort(reverse=False)
for number in numbers:
    print(number)