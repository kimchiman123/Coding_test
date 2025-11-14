def tile(n):
    if n == 0:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1 
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007
    return dp[n] % 10007

n = int(input())
print(tile(n))