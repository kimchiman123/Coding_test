# 해당 방식으로는 결과는 제대로 나온다.
# 하지만 문제의 예시처럼 숫자가 매우 커지는 경우에 파이썬의 부동 소수점 정밀도 문제가 발생
# 그렇기 때문에 매우 큰 경우에는 오류가 발생할 수 있음 
'''
A, B, N = map(int, input().split())
cal = A / B
text = str(cal)
print(text)
result = text[N+1]
print(result)
'''
A, B, N = map(int, input().split())

for _ in range(N):
    A = (A % B) * 10
    # print(A)
    result = A // B
    # print(result)
print(result)