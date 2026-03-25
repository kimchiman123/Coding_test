'''
문제조건: 모든 요청을 배정될 수 있는 경우 요청 금액을 그대로 배정 
모두 배정이 어려운 경우, 이상인 예산요청은 상한액으로 배정
'''
import sys

input = sys.stdin.readline

n = int(input())

budgets = list(map(int, input().split()))
limit = int(input())

budgets.sort()
start = 0 # 제일 작은 값으로 산정
end = budgets[n-1] # 제일 큰 값으로 산정 
# 딱 중간값으로 이분탐색 시작 

max_value = 0
while start <= end:
    total = 0
    mid = (start + end) // 2 
    for i in range(n):
        if budgets[i] <= mid: # 상한액보다 작거나 같으면
            total += budgets[i] # 원래 요청액 그대로 더함
        else: # 상한액을 초과하면
            total += mid # 딱 상한액(mid)까지만 더함

    if total == limit: # 최대값이므로 조기 종료 
        max_value = mid
        break

    if total < limit:
        max_value = max(max_value, mid)
        start = mid + 1
    else:
        end = mid - 1

print(max_value)