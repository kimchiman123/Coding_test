# 미로 (0: 길, 1: 벽)
maze = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 1, 1, 0]
]

# 방문 리스트 초기화
visited = [[False]*4 for _ in range(4)]

def dfs(x, y):
    if x < 0 or x >= 4 or y < 0 or y >= 4:  # 범위를 벗어나는 경우
        return
    if maze[x][y] == 1 or visited[x][y]:  # 벽이거나 이미 방문한 경우
        return
    
    # 현재 위치 방문 처리
    visited[x][y] = True
    print(f"방문: ({x}, {y})")
    
    # 상하좌우 이동
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)

# 시작점에서 DFS 수행
dfs(0, 0)
