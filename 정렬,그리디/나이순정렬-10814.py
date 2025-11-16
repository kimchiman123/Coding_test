'''
sorted는 기존 리스트는 유지하고, 새로운 리스트를 리턴하는 형태이다. 
sort는 기존 리스트에 정렬된 내용을 그대로 저장하는 형태.
위의 두 개의 메서드 모두 안정정렬(같은 key_value인 경우 들어온 순서를 보장)
이를 잘 알아두어야 한다.
'''
n = int(input())

tables = []
for i in range(n):
    age, name = input().split() # age를 기준으로 할거임으로 int로 변경 필요 
    tables.append([int(age), name])

tables.sort(key = lambda x: x[0])
for item in tables:
    print(*item)