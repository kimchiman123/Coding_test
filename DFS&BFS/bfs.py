from collections import deque

def solution(maps):
    n = len(maps) # 행
    m = len(maps[0]) # 열
    
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True # 시작지점이므로 도착처리
    
    queue = deque([(0, 0, 1)]) # ([(0, 0, 1)])
    
    while queue:
        x, y, depth = queue.popleft() # 다음 탐색할 내용물 뽑기 
        if x == n-1 and y == m-1:
            return depth 
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]: # 갈 수 있는 경우 
                    visited[nx][ny] = True 
                    queue.append((nx, ny, depth + 1))
    return -1
