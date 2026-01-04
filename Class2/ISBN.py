import sys

input = sys.stdin.readline

isbn = input().strip()

total = 0
flag = -1
for i in range(len(isbn)):
    if i % 2 == 0:
        if isbn[i] == '*':
            flag = 0
            continue
        total += int(isbn[i])
    else:
        if isbn[i] == '*':
            flag = 1
            continue
        total += int(isbn[i]) * 3

if flag:
    for i in range(10):
        if (10 -(total+(i*3)) % 10) == 10:
            print(i)
            break
else:
    for i in range(10):
        if (10 -(total+i) % 10) == 10:
            print(i)
            break