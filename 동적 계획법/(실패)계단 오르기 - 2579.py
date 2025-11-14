# 해당 배열에서 얻을 수 있는 최댓값을 구한다. 
# 규칙  
# 1. 1계단 또는 2계단만 오르는 것을 허용한다.
# 2. 연속으로 3계단은 허용하지 않음
# 3. 마지막 배열은 반드시 사용 

def stair(array, N):
    jump = 0
    count = 0 # 3회 연속으로 1칸인 경우 2칸 점프
    dp = [0] * (N+1)
    if count == 2: #1칸 점프를 모두 사용
        d[i] += array


    


N = int(input()) # N는 계단의 개수 

# arr = [(int(n) for n in input().split())] # 한 줄에 스플릿하여 입력을 받는 경우에 이렇게 작성 
arr = [0] * N # 함수 배열 생성

for i in range(N): # 입력을 위한 반복
    arr[i] = int(input())

stair(arr, N)