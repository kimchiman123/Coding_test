# 요세푸스 문제 0
import sys
from collections import deque 
input = sys.stdin.readline 

n, k = map(int, input().strip().split())

dq = deque(range(1, n+1))
result = []

while dq:
    for _ in range(k):
        dq.append(dq.popleft()) # 왼쪽 데이터를 오른쪽으로 옮김 
    result.append(dq.pop())

print('<'+', '.join(map(str,result))+'>')