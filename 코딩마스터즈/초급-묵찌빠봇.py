'''
1 - 가위
2 - 바위
3 - 보
'''


import sys 

input = sys.stdin.readline
i = 0
n , m = map(int, input().split())

bot_1 = list(map(int, input().split()))
bot_2 = list(map(int, input().split()))

while True:
    # 먼저 누가 먼저 할지? 
    #print(i)
    if i <= m:
        print(0)
        break
    if (bot_1[i] == 1 and bot_2[i] == 3) or (bot_1[i] == 2 and bot_2[i] == 1) or (bot_1[i] == 3 and bot_2[i] == 2): # 이기는 경우 
        i +=1 
        if bot_1[i] == bot_2[i]:
            print(1)
            break
        else: i += 1
    elif bot_1[i] == bot_2[i]: # 같은 경우 
        i +=1
        continue
    else: #지는 경우 
        i +=1
        if bot_1[i] == bot_2[i]:
            print(2)
            break
        else: i +=1
    