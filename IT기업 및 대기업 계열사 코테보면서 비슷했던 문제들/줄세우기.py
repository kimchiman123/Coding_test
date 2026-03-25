import sys 

input = sys.stdin.readline 

n = int(input())

for _ in range(n):
    data = list(map(int, input().strip().split()))
    case_num = data[0] # 테스트 케이스 번호
    heights = data[1:] # 키 부분 
    count = 0

    for i in range(n):
        for j in range(n+1):
            if heights[i] < heights[j]:
                heights[i], heights[j] = heights[j], heights[i]
                  
                break # 찾고 변경했으므로 종료 
    
    print(heights)
    print(count)
