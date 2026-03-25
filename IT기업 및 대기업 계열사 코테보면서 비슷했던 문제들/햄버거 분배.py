'''
n -> 배열의 길이
k -> 먹는 위치
'''
import sys

input = sys.stdin.readline 

n, k = map(int, input().strip().split())
bench = list(input())
count = 0

for i in range(n - k):
    if bench[i] == 'P': #사람인 경우
        for j in range(i - k, i + k + 1, 1): # k범위 만큼 탐색
            print(f"탐색범위: {i, j}")
            if j >= 0 and j <= n -1 and bench[j] == 'H':
                count += 1
                bench[j] = 'E'

print(bench)
print(count)