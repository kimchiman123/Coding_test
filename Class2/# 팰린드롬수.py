# 팰린드롬수 
import sys

input = sys.stdin.readline

while True:
    num = input().strip()
    if not int(num):
        break
    if num == num[::-1]:
        print("yes")
    else: print("no")