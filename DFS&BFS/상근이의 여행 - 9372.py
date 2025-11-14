n = int(input())
array = []
max_value = 0
for _ in range(n):
    user_input = int(input())
    array.append(user_input)

array.sort(reverse=True) # 정렬 완료 

for i in range(0, len(array)):
    weight = array[i] * (i+1)
    max_value = max(weight, max_value)

print(max_value)