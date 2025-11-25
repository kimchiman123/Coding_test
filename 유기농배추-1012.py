'''
가로, 세로, 배추의 개수

그리고 배추의 좌표를 제공 
'''
import sys
def dfs(x, y, depth):
    if x < 0 or m >= x or y < 0 or n >= y:
        return 0
    if x == n and y == m:
        return depth 
    if mazes[x][y] == 0:
        return
    visited[x][y] = 1 # 방문처리

    # 상하좌우
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if mazes[nx][ny] == 0:
            continue
        count = dfs(nx, ny, depth+1)
    
    visited[x][y] = 0
    return count

input = sys.stdin.readline

n, m = map(int, input().split())
mazes = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0]*m for _ in range(n)] # 방문 배열 생성

print(dfs(0, 0, 0)) # x, y, depth
# print(mazes)
# print(visits)





