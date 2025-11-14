testCase = int(input())  

result = []
for _ in range(testCase):
    num = int(input())  # 의상의 개수 입력
    clothes = {}

    for _ in range(num):
        item, category = input().split()  # 의상의 이름

        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1
    
   
    combinations = 1  # 기본 1
    for count in clothes.values():
        combinations *= (count + 1)

    result.append(combinations - 1)

for res in result:
    print(res)
