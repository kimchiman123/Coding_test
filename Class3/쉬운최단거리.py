'''
# 쉬운 최단 거리
1. 입력받고, 시작점인 2를 찾는 로직 
2. 각 이동할 때마다 depth를 저장 
3. visit배열은 0이면 방문 X, 1이상이면 현재 깊이를 저장 
'''
import sys
from collections import deque 

input = sys.stdin.readline 

n, m = map(int, input().strip().split())
graph = []
visited = [[0]*m for _ in range(n)]
cnt_graph = [[0]*m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().strip().split())))

# target point search 
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            q = deque([(i, j, 1)])
            visited[i][j] = 1
            break
    else:
        continue 
    break         

while q:
    x, y, depth = q.popleft()

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                cnt_graph[nx][ny] = depth
                visited[nx][ny] = 1
                q.append((nx, ny, depth+1))
                continue
        
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt_graph[i][j] = -1
            
for line in cnt_graph:
    print(*line)