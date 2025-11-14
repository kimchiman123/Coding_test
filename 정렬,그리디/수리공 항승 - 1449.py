N, L = map(int, input().split())

# 1. 테이프는 자르는 것이 불가능하다. 
# 2. 테이프를 겹치는 것이 이득이 있다면 상관없다.

count = 0
hoi = 0
points = list(map(int, input().split()))

points.sort()

while True:
    if len(points) == 0:
        break

    if len(points) >1 and points[0] + 1 == points[1]: # 붙이는 위치가 연속인 경우
        points.pop(0)
        if hoi == L - 1:
            count += 1
            hoi = 0 
        else:
            hoi += 1    
    else: #연속이 아닌 경우
        count +=1
        if len(points) > 0:
            points.pop(0)

print(count)