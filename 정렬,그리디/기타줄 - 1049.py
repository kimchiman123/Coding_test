'''
N, M = map(int, input().split()) # N는 기타줄, M은 브랜드의 갯수(배열의 크기)

N1 = N / 6
print(N1)
if N1 <= 1:
    N1 = 0
else: 
    int(N1)
N2 = N % 6 

print(N1, N2)
# array [N][2]
array = [[0 for _ in range(2)] for _ in range(M)]

for i in range(M):
    array[i][0], array[i][1] = map(int, input().split())

for i in range(M):
    set = array[i][0]
    piece = array[i][1]
#    if set > N * piece:
'''
import math

N, M = map(int, input().split()) # N는 기타줄, M은 브랜드의 갯수(배열의 크기)
array = [[0 for _ in range(2)] for _ in range(M)]
N1 = N//6
N1_upper = math.ceil(N1)
N2 = N % 6

print(f"N1: {N1}, N2: {N2}")
for i in range(M):
    array[i][0], array[i][1] = map(int, input().split())

result = []
set= [col[0] for col in set] 
print(set)
piece = array[i][1]
if set * N1 + piece * N2 < set * N1_upper: # 세트를 사는 것이 저렴한 경우 
    result.append(set * N1_upper)
else: 
    result.append(set * N1 + piece * N2)

print(result)
print(min(result))