# 스택
import sys
from collections import deque 

input = sys.stdin.readline

n = int(input())
q = deque()

temp = []
for _ in range(n):
    command = input().strip().split()
    if command[0] == "push":
        q.append(command[1])
    elif command[0] == "pop":
        if q:
            print(q.pop())
        else: print(-1)
    elif command[0] == "size":
        print(len(q))
    elif command[0] == 'empty':
        if q:
            print(0)
        else: print(1)
    elif command[0] == 'top':
        if q:
            print(q[-1])
        else: print(-1)