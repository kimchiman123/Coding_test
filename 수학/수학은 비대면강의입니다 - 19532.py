arr = [int(x) for x in input().split()] # 배열을 입력과 동시에 설정하는 입력 방식 

found = False
for i in range (-999, 1000):
    for j in range (-999, 1000):
        if(arr[0] * i + arr[1] * j == arr[2] and arr[3] * i + arr[4] * j == arr[5]): 
        # 두 개의 연립 방정식이 일치하는 경우에 조건문 동작 
            print(i, j)
            found = True # 중첩 반복문 탈출을 위하여 true로 변경 
            break
    if found: # 첫 번쨰 for문 탈출 
        break

        