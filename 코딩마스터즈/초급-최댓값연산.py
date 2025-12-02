import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
arr.sort(reverse=True)

temp = [0, max(arr), min(arr)]
val1, val2, val3 = max(temp[0], temp[1]), max(temp[1], temp[2]), max(temp[2], temp[0])
result = [val1, val2, val3]
# print(*result, *arr)
if result == arr:
    print("possible")
else: print("impossible")
