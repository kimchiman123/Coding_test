def calculation(n):
    if n <= 1:
        return 1
    else:
        return n * calculation(n - 1)

N = int(input())
print(calculation(N))