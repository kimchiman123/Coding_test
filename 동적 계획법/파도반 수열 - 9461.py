def calu(num):
    dp = [0] * (num+1)
    if num < 3:
        return 1
    dp[1] = 1 
    dp[2] = 1
    dp[3] = 1 

    for i in range(4, num+1):
        # print(dp[i])
        dp[i] = dp[i-2] + dp[i-3]
    return dp[num]
n = int(input())
result = []
for _ in range(n):
    case = int(input())
    result.append(calu(case))

for item in result:
    print(item)