import math

N = int(input())

for _ in range(N):
    array = list(map(int, input().split()))
    
    gcd_array = []
    size = array[0]

    for i in range(1, size):
        gcd= math.gcd(array[i], array[i+1])
        if gcd not in gcd_array:
            gcd_array.append(gcd)
            
    for item in gcd_array:
        print(item)
