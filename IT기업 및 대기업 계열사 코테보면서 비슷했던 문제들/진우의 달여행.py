'''
진우의 달 여행 - 17474
지구 -> 달까지의 최소 이동 비용 
BFS또는 DP를 사용하는 것이 좋아보임 
먼저 DP먼저 해보고 안되면 BFS로 전환해서 풀어보자 
'''

import sys

input = sys.stdin.readline 

N, M = map(int, input().split())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

dp = [[0]*M for _ in range(N)]

# DP배열 초깃값 설정 
for i in range(M):
    dp[0][i] = matrix[0][i]

for i in range(1, N):
    for j in range(M):
        if j - 1 < 0: # 좌측 밖으로 나가는 경우 
            dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
        elif j + 1 >= M: 
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + matrix[i][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) + matrix[i][j] 

print(dp)