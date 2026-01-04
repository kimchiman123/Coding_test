import sys
from collections import deque 

def dfs(v, depth):
    result = []
    if depth == n:
        return print(result)     
    
def bfs(v):
    q = deque([])
input = sys.stdin.readline 

n, m, v = map(int, input().strip().split())

graph = [[] for _ in range(n)]
visited = [[0]*m for _ in range(n)]

for _ in range(m):
    key, val = map(int, input().strip().split())
    graph[key].append(val)
    graph[val].append(key) # 양방향인 경우 추가 

dfs()
