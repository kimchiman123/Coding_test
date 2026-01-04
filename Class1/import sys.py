import sys

input = sys.stdin.readline 

numbers = list(map(int, input().strip().split()))

if numbers[0] > numbers[1]: # 감소해야 하는 경우
    for i in range(len(numbers) - 1):
        if numbers[i] <= numbers[i+1]:
            print("mixed")
            break
    else: # 
        print('descending')
else: # 증가해야 하는 경우 
    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i+1]:
            print("mixed")
            break 
    else:
        print("ascending")
