'''
0과 1의 총 호출 횟수를 출력한다.  
전역으로 두고 풀까?
재귀로 처리 시, 시간 초과가 발생 함, dp배열로 대체하여 풀이 
그런데 dp는 이전 합을 계속 더하면 푸는것 아닌가? 
그러면 어카지...
'''
def fibonacci(n):
    zero_dp = [0] * (n+1) # 재귀로 처리 시, 시간 초과가 발생 함, dp배열로 대체하여 풀이 
    one_dp = [0] * (n+1)

    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1
    zero_dp[0] = 1; one_dp[0] = 0
    zero_dp[1] = 0; one_dp[1] = 1

    for i in range(2, n+1):
        zero_dp[i] = zero_dp[i-1] + zero_dp[i-2]
        one_dp[i] = one_dp[i-1] + one_dp[i-2]
        # dp배열로 변환하여, 각각 경우를 dp로 처리 
    return zero_dp[n], one_dp[n]

k = int(input())

for _ in range(k):
    print(*fibonacci(int(input())))
    
