import sys

def dfs(x, y):
    visited[x][y] = 1
    cnt = 1

    # 각 뭉태기마다의 탐색을 수행 
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0 ,0]
    for i in range(4):    
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                cnt +=dfs(nx, ny)
    return cnt

input = sys.stdin.readline

n = int(input())

graph = []
result = []
visited = [[0]*n for _ in range(n)]

# 입력부분 
for _ in range(n):
    graph.append(list(map(int, input().strip())))


for i in range(n):
    for j in range(n):
        # 현재 방문하지 않고, 1인 경우 단지이므로 카운팅 
        if not visited[i][j] and graph[i][j] == 1:
            count = dfs(i,j)
            result.append(count)

# 출력부
result.sort()
print(len(result))
for item in result:
    print(item)