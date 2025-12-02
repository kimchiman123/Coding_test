'''
공급가의 10%으로 더해서 완성 
29900 = 27182 + 2718로 완성 


'''
import sys
import math
input = sys.stdin.readline

n = int(input())

supply_price = round(n / 1.1)
tax = math.floor((supply_price / 10))

if supply_price + tax != n:
    print(-1)
else:
    print(supply_price, tax)


# 필요하면 다시 /10 해서 출력

#print(sp/10+tx/10, n)
#if sp + tx == n:
#    print(sp, tx)
#else: print(-1)

