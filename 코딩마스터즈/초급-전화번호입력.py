import sys 

input = sys.stdin.readline

phone_number = input().strip().split('-')

# 블럭이 3개가 아니거나, 시작이 010이 아니면 제거거
if len(phone_number) != 3 or phone_number[0] != '010': 
    print("invalid")
    sys.exit(0)   

for number in phone_number:
    #print(number.isdigit(), len(number) <= 4)
    if number.isdigit() and len(number) <= 4:
         continue
    else:
        print("invalid")
        sys.exit(0)

print("valid")