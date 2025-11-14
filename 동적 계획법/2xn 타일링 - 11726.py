def tile(n):
    dp = [0] * (n + 1) # n의 크기만큼 사용할 수 있도록 배열을 생성 
    dp[0] = 0
    dp[1] = 1 
    if n <= 1:
        return dp[n]
    else:
        if n == 2:
            return 2 
        else:
            dp[2] = 2 # n = 1인 경우 인덱스를 초과하기 때문에 따로 처리 
    for i in range(3, n + 1):
        # 점화식
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    return dp[i] # 계산결과 반환
 
n = int(input())
print(tile(n)) 