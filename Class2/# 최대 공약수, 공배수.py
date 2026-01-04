# 최대 공약수, 공배수 

import sys

input = sys.stdin.readline 

a, b = map(int, input().strip().split())
gcd = 1
for i in range(1, min(a,b)+1):
    if a % i == 0 and b % i == 0:
        gcd = i

lcm = (a * b) // gcd

print(gcd)
print(lcm)