import sys
import math
input = sys.stdin.readline

p, n = map(int, input().split())
zero_cnt = 0

number = math.factorial(n)
print(number)
flag = 1
while number >= p:
    if number % p == 0 and flag == 1:
        zero_cnt += 1
        flag = 1
    else: flag = 0
    number = number // p
print(zero_cnt)


