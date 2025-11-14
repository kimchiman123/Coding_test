import sys

def knapsack(N, K, items):
    # DP 테이블 초기화
    dp = [0] * (K + 1)

    # 물건을 하나씩 확인
    for W, V in items:
        # **뒤에서부터** 갱신 (0-1 배낭 문제)
        for w in range(K, W - 1, -1):
            dp[w] = max(dp[w], dp[w - W] + V)

    return dp[K]

# 입력 처리
N, K = map(int, sys.stdin.readline().split())
items = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 결과 출력
print(knapsack(N, K, items))
