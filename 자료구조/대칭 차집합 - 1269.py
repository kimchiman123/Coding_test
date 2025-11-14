def cal(array1, array2):
    return len(list(set(array1) - set(array2)))

A, B = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(cal(arr1, arr2) + cal(arr2, arr1))
