roomNumber = input() 

plastic_num = [0] * 10

for char in roomNumber:
    num = int(char)  # 각 문자를 정수로 변환
    plastic_num[num] += 1
plastic_num[6] = plastic_num[9] = (plastic_num[6] + plastic_num[9] +1 ) // 2
        
print(max(plastic_num))
