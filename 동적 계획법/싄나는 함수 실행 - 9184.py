# 조건에 따라서 실행할 내용을 결정정
def calculation(array):
    
    for i in range(0, 6):
        if array[i][0] <= 0 or array[i][1] <= 0 or array[i][2] <= 0: # 1번 조건, 0보다 작거나 같다
            print()
        elif array[i][0] > 20 or array[i][1] > 20 or array[i][2] > 20: # 2번 조건, 20보다 크면 20으로 통일 
            print()
        elif array[i][0] < array[i][1] and array[i][1] < array[i][2]:
            print()
        elif array[i][0] == - 1 and array[i][1] == -1  and array[i][2] == -1: # 모든 입력 -1인 경우 씹는다. 
            continue
        else:
            print()
   
    for i in range(0, 6):
        print(f"w({array[i][0]}, {array[i][1]}, {array[i][2]}) = ")

# 실제 계산을 진행할 함수, DP
def w(a, b, c):
    if a == -1 and b == -1 and c == -1:
        return None
    MAX = 20 # 실질적으로 20이 넘어가면 모두 20으로 설정되므로 최댓값을 20 
    dp = [0] * 20 
    dp[0] = 
    dp[1] = 
array = []

# 배열을 입력 
for i in range(6):
    row = list(map(int, input().split()))
    array.append(row)

print(array)
print(calculation(array))