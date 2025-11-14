def cal(array1, array2):
    
        




N1 = int(input())
array1 = list(map(int, input().split()))
N2 = int(input())
array2 = list(map(int, input().split()))

if len(array1) < len(array2):
    cal(array2,array1)
else:
    cal(array1, array2)