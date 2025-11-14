import math

N = int(input())

array = [0] * N 
array = list(map(int, input().split()))

for i in range(1, len(array)):
    gcd = math.gcd(array[0], array[i])
    print(f"{int(array[0]/gcd)}/{int(array[i]/gcd)}")