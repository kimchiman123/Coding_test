import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == 1: # 뭉테기의 일부인 경우 
        graph[x][y] = 0 # 갯수를 카운트 했으므로 삭제 
        # dfs를 통하여 연결된 모든 뭉테기를 서치함 
        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x-1, y)
        return True 
    return False 

input = sys.stdin.readline

T = int(input()) # 테스트 케이스 

for _ in range(T):
    m, n, k = map(int, input().strip().split()) 
    graph =[[0]*(m+1) for _ in range(n)]
    
    for _ in range(k):
        col, row = map(int, input().strip().split()) 
        graph[row][col] = 1 
    
    count = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                count += 1
    print(count)

    