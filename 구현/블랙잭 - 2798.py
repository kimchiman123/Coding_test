from itertools import combinations

# 입력 받기
N, M = map(int, input("카드 개수 N과 목표 M을 입력하세요: ").split())
cards = list(map(int, input("카드에 쓰인 숫자를 입력하세요: ").split()))

# 가능한 3장 조합 생성
card_combinations = combinations(cards, 3)

# 합이 M을 넘지 않는 조합 중 최대값 찾기
max_sum = 0
for combination in card_combinations:
    print(combination)
    total = sum(combination)
    if total <= M:
        max_sum = max(max_sum, total)

# 결과 출력
print(max_sum)
