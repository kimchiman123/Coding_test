# 괄호
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

numbers = []
counts = []
for _ in range(n):
    numbers.append(int(input().strip()))
counter = Counter(numbers)
max_count = max(counter.values())

for num, freq in counter.items():
    if freq == max_count:
        counts.append(num)
counts.sort()
numbers.sort()
print(round(sum(numbers)/len(numbers)))
print(numbers[len(numbers)//2])
if len(counts) > 1:
    print(counts[1])
else: print(counts[0])
print(max(numbers) - min(numbers))