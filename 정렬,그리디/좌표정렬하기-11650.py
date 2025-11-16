n = int(input())

tables = []
for i in range(n):
    x, y = map(int, input().split())  
    tables.append([x, y])

tables.sort(key = lambda x: (x[0], x[1])) # x[0]를 먼저 비교하고, 그 후 같은 value는 x[1] value값으로 정렬 
for item in tables:
    print(*item)