import sys
import math

def is_prime(num):
    if num < 2: # 2미만은 소수 x
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: # 나누어지는 경우 소수 
            return False
    return True

input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().strip().split()))
count = 0
for i in range(len(numbers)):
    if is_prime(numbers[i]):
        #print(numbers[i])
        count += 1

print(count)