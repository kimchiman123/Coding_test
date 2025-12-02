import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
offset = 25 
def dfs(x, y, current_dir, depth):
    if depth == n:
        return 1
    
    total_count = 0
    
    for rotate in [-1, 1]:
        next_dir = (current_dir + rotate) % 4
        nx = x + dx[next_dir]
        ny = y + dy[next_dir]
        
        if not visited[nx + offset][ny + offset]:
            visited[nx + offset][ny + offset] = True  # 방문 체크
            total_count += dfs(nx, ny, next_dir, depth + 1)
            visited[nx + offset][ny + offset] = False # 백트래킹
            
    return total_count

n = int(input())

visited = [[False] * 55 for _ in range(55)]

# 시작점 방문 처리
visited[0 + offset][0 + offset] = True
visited[0 + dx[0] + offset][0 + dy[0] + offset] = True # 첫 한칸(북쪽) 이동 처리

print(dfs(0, 1, 0, 1))