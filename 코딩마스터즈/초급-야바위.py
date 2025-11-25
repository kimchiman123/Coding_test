import sys 

input = sys.stdin.readline

n, m = map(int, input().split())

numbers = [i for i in range(1, n + 1)]

for i in range(m):
    # print(i)
    front, back = map(int, input().split())
    numbers[front-1], numbers[back-1] = numbers[back-1], numbers[front-1]
    print(numbers)
    
#print(numbers)
find = int(input())
print(numbers.index(find) + 1)





