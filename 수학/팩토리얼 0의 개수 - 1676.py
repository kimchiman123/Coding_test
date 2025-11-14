def calculation(n):
    # 동적 프로그래밍으로 처리 
    if n == 0:
        return -1
    
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = i * dp[i - 1]
        
    return dp[n]
   
def count_zeros(text):
    count = 0

    for i in range(len(text) -1, -1, -1): # -1씩 감소하며, -1까지 반복한다.
        if text[i] == '0':
            count += 1
        else:
            break
    
    return count
N = int(input())
text = str(calculation(N)) # 정수형이기에 문자열로 변환
print(count_zeros(text))