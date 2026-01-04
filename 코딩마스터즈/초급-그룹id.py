import sys 

input = sys.stdin.readline

arr = list(input().strip() for _ in range(4))
flag = 0
#print(arr)


for i in range(0, 3, 2):      # 0, 2 (시작점)
    for j in range(0, 3, 2):  # 0, 2 (시작점)
        count = 0
        for a in range(2):    # 0, 1
            for b in range(2):# 0, 1
                if arr[i+a][j+b] == 'X':
                    count += 1
        
        if count >= 3:
            flag = 1
            break
    if flag:
        break

if flag:
    print("yes")
else: print("no")