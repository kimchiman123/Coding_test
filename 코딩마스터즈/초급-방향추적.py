import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

for i in range(n-1):
    gap = 0
    if arr[i][0] - arr[i+1][0] != 0: # x좌표의 경우, 
        gap = arr[i+1][0] - arr[i][0]  # 동서, 2와 4만 가능 
        if gap > 0: #동쪽- 2
            print(1, abs(gap))
        else: # 서쪽 - 4
            print(3, abs(gap))
    else:
        gap = arr[i+1][1] - arr[i][1] 
        if gap > 0:
            print(2, abs(gap))
        else:
            print(4, abs(gap))

#elif arr[i][1] - arr[i+1][1] > 0: