# 해당 문제는 n, m, h 모두 10^9이상으로 굉장히 크게 설정함, 최적화가 필수임
import sys

input = sys.stdin.readline 

n, m = map(int, input().strip().split())

array = list(map(int, input().strip().split()))

start = 0
end = max(array)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for tree in array:
        if tree > mid:
            total += tree - mid 
    
    if total < m:
        end = mid - 1 
    else: 
        result = mid 
        start = mid + 1
print(result)