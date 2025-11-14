N = int(input())

serial_num = []

for _ in range(N):
    word = input()
    serial_num.append(word)

# 조건 1: 길이가 다른경우, 짧은것이 우선 
# 조건 2: 자리 수의 합으로 계산 
# 조건 3: 사전순

for _ in range(N):
    for i in range(N-1):
        if len(serial_num[i]) != len(serial_num[i+1]):
            if len(serial_num[i]) > len(serial_num[i+1]): # 두 번쨰 벨류가 큰 경우
                serial_num[i], serial_num[i+1] = serial_num[i+1], serial_num[i]
                
        elif len(serial_num[i]) == len(serial_num[i+1]): 
            sum1 = sum(int(char) for char in serial_num[i] if char.isdigit())
            sum2 = sum(int(char) for char in serial_num[i+1] if char.isdigit())   
            
            if sum1 > sum2:
                serial_num[i], serial_num[i+1] = serial_num[i+1], serial_num[i]

            elif sum1 == sum2:
                if serial_num[i] > serial_num[i+1]:
                    serial_num[i], serial_num[i+1] = serial_num[i+1], serial_num[i]

for item in serial_num:
    print(item)

        
