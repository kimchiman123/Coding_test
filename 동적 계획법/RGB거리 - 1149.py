def RGB(array, N):
    dp = [[0] * 3 for _ in range(N)] # DP배열 설정 
    # 동적배열 초기설정
    dp[0][0] = array[0][0]
    dp[0][1] = array[0][1]
    dp[0][2] = array[0][2]

    for i in range(1, N):
        dp[i][0] = array[i][0] + min(dp[i-1][1], dp[i-1][2]) # Red
        dp[i][1] = array[i][1] + min(dp[i-1][0], dp[i-1][2]) # Blue
        dp[i][2] = array[i][2] + min(dp[i-1][0], dp[i-1][1]) # Green
    result = min(dp[N-1][0], dp[N-1][1], dp[N-1][2]) # 마지막에서 가장 작은 값을 결과로 설정  
    return result 
N = int(input()) 
array = []

for i in range(N):
    row = list(map(int, input().split()))
    array.append(row)

print(RGB(array, N))
