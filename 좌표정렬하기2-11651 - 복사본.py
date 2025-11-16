n = int(input())

numbers = ()
numbers.

for _ in range(n):
    numbers.append(int(input()))

numbers.sort(reverse=False)
for number in numbers:
    print(number)