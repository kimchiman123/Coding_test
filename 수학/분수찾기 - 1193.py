N = int(input())
X, Y = 1, 1
flag = 0
count = 1 
limit = 1
'''
1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> 1/3 -> 1/4 -> 2/3 -> 3/2
'''

while count != N:
    # print(f" 반복문 값: {X}/{Y}")
    if X == limit or Y == limit:
        limit += 1 # 값의 천장을 설정
        if flag == 0: # 변경시 분자/분모의 증/가감도 변경되어야 함
            flag = 1
        else:
            flag = 0

    if flag == 0:
        X += 1
        Y -= 1
        count += 1
        if Y < 1: # 0이 되는 경우 1로 설정정
            Y = 1
    else:
        X -= 1
        Y += 1
        count += 1
        if X < 1:
            X = 1
# print(count)
print(f"{X}/{Y}")