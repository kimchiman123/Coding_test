'''
과일의 종류를 2개로 만드는 경우에서 
총 갯수가 최대인 것을 찾아보자

투 포인터로 앞 뒤로 조절해가면서,
딕셔너리로 저장해두고, 여기에서 종류가 2개면 check수행

-> 그런데 문제가 투 포인터는 값에 따라서 조정되는 건데
해당 문제는 종류를 통하여 조정하는 거이므로 어떻게 해야할까? 
'''

import sys
from collections import Counter

def get_count(check_list): # 카운터 값이 인풋
    # 내용물 갯수
    # 1이상인 것만 골라서 카운팅
    return sum(1 for v in check_list.values() if v > 0)

input = sys.stdin.readline

n = int(input())

fruits = list(map(int, input().split()))
 
start = 0
end = len(fruits) - 1
max_value = 0
print(start, end)

init_value = n

# 투 포인터로 구현
while start <= end: 
    # 갯수를 세기 위한 Counter
    check_list = Counter(fruits[start:end]) # 각 상황마다의 딕셔너리 리스트 생성 
    count = get_count(check_list) # 종류의 갯수
    if count <= 2: # 종류가 2개 이하인 경우
        
# print(f"카운터: {check_list}, 내용물 갯수: {len(check_list)}")
# print(fruits)