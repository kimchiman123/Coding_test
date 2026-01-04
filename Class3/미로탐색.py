import sys
from collections import deque

input = sys.stdin.readline 

n, m = map(int, input().strip().split())

matrix = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]
q = deque((1, 1))
print(q)