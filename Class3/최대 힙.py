# 괄호
import sys
import heapq
input = sys.stdin.readline

heap = []
n = int(input())

result = []
for _ in range(n):
    data = int(input())
    if data == 0:
        if not heap:
            result.append(0)
            continue
        result.append(heapq.heappop(heap))
        continue
    heapq.heappush(heap, -1*data)
    
for num in result:
    print(-1*num)