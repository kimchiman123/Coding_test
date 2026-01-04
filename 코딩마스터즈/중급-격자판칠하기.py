'''
30인 경우 -> 120까지 도착 
3을 더 가야함
307.5였으면 308이였을테니깐... 
'''

import sys

input = sys.stdin.readline

x, y, z = map(int, input().split())
total = 0

while x > 0:
    if x < (y * 2):
        total = total + z -  (x % (y*2))
        x = x - (y * 2)
    else:
        total += z
        x = x - (y * 2)
    
    #print(x, total)
print(total)
