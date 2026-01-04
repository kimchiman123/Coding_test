import sys
from collections import deque 

def solution(array):
    q = deque()
    for item in array:
        if item == '(':
            q.append(item)
        else:
            if not q:  # q가 비어 있다면
                return "NO"
            q.pop()
    if not q:
        return "YES"
    else: return "NO"

input = sys.stdin.readline 

n = int(input())

for _ in range(n):
    array = list(input().strip())
    result = solution(array)
    print(result)
