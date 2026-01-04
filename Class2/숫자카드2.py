import sys

input = sys.stdin.readline

cards = {}
n1 = int(input())
numbers = list(map(int, input().strip().split()))
for num in numbers:
    cards[num] = cards.get(num, 0) + 1
n2 = int(input())
temp = list(map(int, input().strip().split()))

for num in temp: 
    # 키가 있으면 해당 값을, 없으면 0을 반환
    print(cards.get(num, 0), end=' ')
