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

max_value = 0
result = 0
for start in range(n - k + 1):
    end = start + k
    window = visitor[start:end]
    if sum(window) > max_value:
        max_value = sum(window)
        result = start

print(result+1)