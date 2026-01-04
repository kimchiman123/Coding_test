import sys
from collections import deque

def bfs(x, y):
    q = deque([(x, y, 1)])
    visited[x][y] = True 
    
    while q:
        v1, v2, v3 = q.popleft()
        if v1 == n -1 and v2 == m-1:
            return v3
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            nx = v1 + dx[i]
            ny = v2 + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    q.append([nx, ny, v3+1])
                    visited[nx][ny] = True

input = sys.stdin.readline

n, m = map(int, input().strip().split())

graph = []
visited = [[False]*m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().strip())))

count =bfs(0, 0)
print(count)
