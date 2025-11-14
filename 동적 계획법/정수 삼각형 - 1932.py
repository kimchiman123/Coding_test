def triangle_cal(array, n):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    # dp배열 초기설정정
    dp[0][0] = array[0][0]
    dp[1][0] = array[1][0] + dp[0][0]
    dp[1][1] = array[1][1] + dp[0][0]
    for i in range(2, n):
        for j in range(len(array[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + array[i][j]
            elif j == len(array[i]) - 1:
                dp[i][j] = dp[i-1][j-1] + array[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + array[i][j]
        # dp[i][j] = dp[i-1][len(array[i])] + array[i][len(array[i])]
    return max(dp[n-1])
    # return dp 배열 내부 확인용 
    
n = int(input()) # 삼각형의 크기 

array = []

for i in range(n):
    array.append(list(map(int, input().split())))

print(triangle_cal(array, n))
# print(f" 이거임: {triangle_cal(array, n)}") 배열 확인용 