n = int(input())
array = [0] * n

for i in range(n):
    array[i] = int(input())

frist_num = array[0] # 기호 1번번
array.pop(0) # 처리과정에서 1번 원소는 계산에 포함되지 않도록 삭제제
# print(f"{frist_num}: frist_num") # 테스트트
count = 0 
while True:
    if n <= 1:
        break
    if frist_num <= max(array):
        max_index = array.index(max(array)) # 가장 큰 인덱스를 저장 
        array[max_index] -= 1 # 가장 큰 인덱스의 원소를 1 감소 
        frist_num += 1
        count += 1
        # print(f"{array}: array, {frist_num}: frist_num") # 테스트 용용
    else:
        break
    
print(count)