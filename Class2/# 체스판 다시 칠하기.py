# 체스판 다시 칠하기
import sys 

input = sys.stdin.readline
n, m = map(int, input().strip().split())

matrix = []
for _ in range(n):
    matrix.append(list(input().strip()))

min_value = float('inf')
for i in range(n - 7):
    for j in range(m - 7):
        count_w = 0
        count_b = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2== 0: # 행과 열 합이 짝/홀에 따라 색이 변경 필요 
                    if matrix[x][y] != 'W': count_w += 1
                    if matrix[x][y] != 'B': count_b += 1
                else:
                    if matrix[x][y] != 'W': count_b += 1
                    if matrix[x][y] != 'B': count_w += 1
        
        curr_min = min(count_w, count_b)
        if curr_min < min_value:
            min_value = curr_min

print(min_value)