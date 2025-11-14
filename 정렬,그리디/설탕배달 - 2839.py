def sugar(n):
    count = 0
    while n >= 0:
        if n % 5 == 0: # 최선의 경우인 5로 나누는 경우부터 계산
            count += n // 5
            return count
        n = n - 3 # 남은 경우인 3으로 나누는 경우 따로 반복문으로 처리 
        count = count + 1
    return -1

n = int(input())
print(sugar(n))

# GPT가 풀어줌. 따로 공부하자자
# 해당 알고리즘은 탐욕 알고리즘으로 풀이 