import sys

input = sys.stdin.readline

n, score, p = map(int, input().strip().split())

scores = list(map(int, input().strip().split()))
scores.append(score)
scores.sort(reverse=True)

print(scores)
print(scores.index(score)+1)

print(len(scores))
print(p)

