def cal(K, A, DT, RT):
    time = 0
    total = 0
    while total < K:
        for _ in range(DT):
            total += A
            time += 1
            if total >= K: # 반복문 중간에 결과를 만족하는 경우 
                return time
        time += RT
    return time

N, K, A = map(int, input().split()) 
# N = 참가자 수, K = 콜라 용량, A = 1초에 마시는 양 

min_time = float('inf')  # 무한대로 값을 초기화화

for _ in range(N):
    drink_T, rest_T = map(int, input().split()) # 마시는 시간, 쉬는 시간 
    min_time = min(min_time, cal(K, A, drink_T, rest_T))

print(min_time)