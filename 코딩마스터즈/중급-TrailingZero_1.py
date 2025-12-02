import sys 
import math

def trailing_zero(n):
    print(n)
    count = 0
    while n > 0 and n % 10 == 0:
        count += 1
        n //= 10
    print(count)
    return count

input = sys.stdin.readline 

n = int(input())
i = 0
while True:
    if trailing_zero(math.factorial(i)) == n:
        print(i)
        break
    i += 1
