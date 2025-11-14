# dp[0] = 0 
# dp[1] = 3 , dp[2] = 7
# dp[3] = 17, dp[4] = 41
# 기본항: dp[i] = 2*dp[i-1] + dp[i-2]
# 해당 문제에서 메모리 문제 때문에 
# dp배열 대신 변수를 통하여 계산
# DP가 아무리 효율적인 알고리즘이더라도 
# 더 좋은 알고리즘이 존재할 수도 있음!!!

def calculation(N):
    # 초기 설정 값보다 N이 작은경우
    if N == 1:
        return 3
    elif N== 2:
        return 7    
    prev1 = 7
    prev2 = 3
    for _ in range(3, N+1):
        current = (2 * prev1 + prev2) % 9901
        prev2 = prev1
        prev1 = current
    return current
 
N = int(input()) # 우리의 크기 
print(calculation(N)) #결과출력 