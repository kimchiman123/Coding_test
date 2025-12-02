import sys 
import itertools

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
flag = 0
for combi in itertools.combinations(arr, 4):
    for i in range(4):
        #print(combi[i%4], combi[(i+1)%4], combi[(i+2) % 4], combi[(i+3) % 4])
        if combi[i%4] * combi[(i+1)%4] == combi[(i+2) % 4] * combi[(i+3) % 4]:
            flag = 1
    
if flag:
    print("yes")
else: print("no")