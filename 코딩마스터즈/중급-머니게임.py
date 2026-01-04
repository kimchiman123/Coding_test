'''
1. 둘 중 한명이 0이 되면 게임 종료 else: 2번으로 
2. if 민서*2 > 윤호 -> 민서 - (윤호*2) else: 3번 
3. if 윤호*2 > 민서 -> 윤호 - (민서*2) else: 종료 
3번에서 수행되지 않으면 종료  
'''
import sys

input = sys.stdin.readline

def state_1():
    # n 또는 m이 0이면 종료 신호(0), 둘 다 양수면 진행(1)
    return 0 if n <= 0 or m <= 0 else 1

def state_2():
    # n, m을 이용해 어떤 연산을 하고, 계속할지(0)/넘길지(1) 결정
    global n, m
    if n * 2 > m:
        n = n - (m * 2)
        return 0  # 계속 while 루프 진행
    else:
        return 1  # state_3로 넘김

def state_3():
    global n, m
    if m * 2 > n:
        m = m - (n * 2)
        return 0  # 계속 while 루프 진행
    else:
        return 1  # 최종 종료 신호로 해석

n, m = map(int, input().split())

while True:
    # 1단계: 종료 조건 체크
    if state_1() == 0:
        print(n, m)
        break

    # 2단계: state_2 실행
    if state_2() == 0:
        # state_2 단계에서 처리가 끝났으므로 다음 루프로
        continue
    else:
        # 3단계: state_3 실행
        if state_3() == 0:
            # state_3에서 처리 후 계속
            continue
        else:
            # state_3가 1을 반환하면 완전 종료
            print(n, m)
            break
