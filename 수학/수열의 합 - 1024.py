from itertools import combinations, groupby

N, L = map(int, input().split())

array = [0] * 100 # 최대 길이는 100이다. 
result = []
flag = 0
for i in range(0, 100):
    array[i] = i
for r in range(L, 100):
    for comb in combinations(array , r):
        if all(comb[i] + 1 == comb[i + 1] for i in range(len(comb) - 1)): # 연속적인 경우 확인
            if sum(comb) == N:
                result = comb
                flag = 1
                break
    if flag:
        break

print(result)

'''
N, L = map(int, input().split())

# L부터 100까지 길이를 증가시키며 탐색
for l in range(L, 101):
    # 등차수열의 합 공식에서 시작 값 a 계산
    a = (N - (l * (l - 1)) // 2) / l
    if a.is_integer() and a >= 0:  # a가 정수이고 음이 아닌 경우
        a = int(a)
        result = [a + i for i in range(l)]
        print(*result)
        break
else:
    print(-1)  # 조건을 만족하는 수열이 없는 경우


'''