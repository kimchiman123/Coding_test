number_list = []
def self_num(number):
    sum = 0
    for char in str(number): # 각 자리수 계산산
        n = int(char)
        sum += n
    return sum + number # 원래 수와 자리수 리턴턴

for i in range(10000):
    number_list.append(self_num(i))

for i in range(10000):
    if i in number_list: # 셀프넘버 리스트에 있는 경우 패스
        continue
    print(i)