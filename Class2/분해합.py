import sys

input = sys.stdin.readline
number = int(input().strip())

for i in range(1, number + 1):
    total = i + sum(map(int, str(i)))
    
    if total == number:
        print(i)
        sys.exit() 

print(0)