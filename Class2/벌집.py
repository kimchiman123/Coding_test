import sys

input = sys.stdin.readline 

n = int(input())
count = 1
cnt = 1
ceil = 6
for i in range(1, n):
    #print(cnt)
    count += 1
    for j in range(ceil):
        #print(f"check: {cnt}")
        if cnt == n-1:
            print(count)
            sys.exit()
        cnt +=1
    ceil = ceil + 6