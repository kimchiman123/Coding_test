import sys
from collections import deque 

n, m = map(int, input().strip().split())

graph = []
visited = [[0]*m for _ in range(n)]
cnt = 0
for _ in range(n):
    graph.append(list(input().strip()))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            q = deque([(i, j)])
            visited[i][j] == 1
            break
    else:
        continue
    break 

while q:
    x, y = q.popleft()

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] != 'X' and not visited[nx][ny]:
                #print(nx, ny)
                if graph[nx][ny] == 'P':
                    cnt += 1
                visited[nx][ny] = 1
                q.append((nx, ny))

#print(visited)
#print(cnt)
if cnt:
    print(cnt)
else: print('TT')