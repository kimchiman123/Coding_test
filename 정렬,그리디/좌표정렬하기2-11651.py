n = int(input())

tables = []
for i in range(n):
    x, y = map(int, input().split())  
    tables.append([x, y])

tables.sort(key = lambda x: (x[1], x[0])) # 이건 x[1], x[0] 위치만 변경해서 수행.
for item in tables:
    print(*item)