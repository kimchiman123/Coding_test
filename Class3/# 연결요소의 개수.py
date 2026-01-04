# 연결요소의 개수 
import sys 

result = 0
def dfs():
    # 더 연결한 요소가 없는 경우 
    if graph[]
    return 1

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visit = [[0]*m for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(graph)
print(visit)