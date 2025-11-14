def find_nth_end_number(n):
    count = 0
    num = 666  # 가장 작은 종말의 수
    
    while count < n:
        if '666' in str(num):  # 숫자에 '666'이 포함되어 있는지 확인
            count += 1
        num += 1  # 다음 숫자로 이동

    return num - 1  # 마지막 증가한 값에서 1을 빼서 정확한 값 반환

# 입력 받기
n = int(input())
print(find_nth_end_number(n))

# 뭔소리인지 잘 모르겠음....
# 다시 확인인