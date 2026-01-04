import sys

def find_heart():
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == '*':
                return i+1, j
            
input = sys.stdin.readline

n = int(input())
# print(n)

matrix = []
for _ in range(n):
    matrix.append(list(input().strip()))

# 먼저 심장의 좌표를 찾는 로직
heart_x, heart_y = find_heart()

# 왼쪽 손 
left_hand = 0
for i in range(heart_x):
    if matrix[i][heart_y] == '*':
        left_hand += 1

right_hand = 0
for i in range(heart_x+1, n, 1):
    if matrix[i][heart_y] == '*':
        right_hand +=1 
print(heart_x+1, heart_y+1)
print(left_hand, right_hand)