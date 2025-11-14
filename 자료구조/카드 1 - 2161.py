from collections import deque

N = int(input())
queue = []
waits = []
for i in range(1, N+1):
    queue.append(i)

for _ in range(N):
    if queue and queue[0] % 2 == 0:
        waits.append(queue.pop(0))
    else:
        if queue:
            temp = queue.pop(0)
            queue.append(temp)

for wait in waits:
    queue.append(wait)
print(queue)
