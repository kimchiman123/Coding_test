# 색종이 만들기 
# 가장 작은 단위부터 잘라가면서 올라가자 
import sys

input = sys.stdin.readline

n = int(input())

matrix = [list(map(int, input().strip().split())) for _ in range(n)]

print(matrix)