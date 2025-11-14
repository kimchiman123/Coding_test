from collections import deque

# 미로 (0: 길, 1: 벽)
maze = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 1, 1, 0]
]

# 방문 리스트 초기화
visited = [[False]*4 for _ in range(4)]

def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    
    while queue:
        x, y = queue.popleft()
        print(f"방문: ({x}, {y})")
        
        # 상하좌우 이동
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx][ny] and maze[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = True

# 시작점에서 BFS 수행
bfs(0, 0)
