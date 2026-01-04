'''
N일이 주어지는데, 
연속된 K값을 제외하고 평균 방문자를 최대로 만들고 싶어함 
[1, 2, 3, 4, 5, 6]이고, K가 3인 경우 
[4, 5, 6]이렇게 포함하면 최대가 된다. 슬라이딩 윈도우로 최대값을 찾는다. 
'''
import sys 
input = sys.stdin.readline

n, k = map(int, input().split())
visitor = list(map(int, input().split()))

max_value = -1 # 슬라이싱한 배열이 가장 큰지를 판단 
result = 0 # 최종 출력값
for start in range(n - k + 1):
    end = start + k # window사이즈를 설정 
    window = visitor[start:end] # 설정 크기만큼 슬라이싱 
    if sum(window) > max_value: # 가장 큰 배열인 경우 
        # 새로운 값으로 업데이트 
        max_value = sum(window)
        result = start

print(result+1)

cur_sum = sum(visitor[:k])
max_value = cur_sum
result = 0

for start in range(1, n - k + 1):
    cur_sum = cur_sum - visitor[start - 1] + visitor[start + k - 1] # 전체에서 
    if cur_sum > max_value:
        max_value = cur_sum
        result = start