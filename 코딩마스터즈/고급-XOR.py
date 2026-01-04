import sys 
from itertools import combinations
input = sys.stdin.readline

def calculation_xor(combi: list):
    result = 0
    for item in combi:
        result = result ^ item
    
    return result
    
n = int(input())
count = 0
numbers = list(map(int, input().split()))

for i in range(2, n+1):  # n번까지 출력되야 하므로 n+1까지 수행 
    for combi in combinations(numbers, i): 
        count+=1

print(count)