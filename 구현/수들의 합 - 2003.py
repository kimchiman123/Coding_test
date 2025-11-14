# from itertools import combinations
# 콤비네이션으로 풀려고 하였으나, 문제의 조건은 연속적인 배열을 처리해야 하므로 실패패

N, target =map(int, input().split()) # N과 target을 입력 받는다. 
array = list(map(int, input().split()))

start = 0
end = 0
sum = 0
count = 0

# 투 포인터 알고리즘 
# 포인터를 이동시키며 값에 따라서 시작 포인터를 조정하여 사용한다.
while end < N: #배열의 크기 만큼 반복 
    sum = sum + array[end]

    while sum > target and start <= end: 
        # 시작 포인터와 끝 포인터는 배열을 지정하는 간격이다. 
        # 그러므로 target보다 합이 더 크면 더한 수를 빼고 
        # 포인터 크기를 재지정하여 반복한다.
        sum = sum - array[start]
        start += 1
    
    if sum == target:
        count += 1
    
    end += 1

print(count)