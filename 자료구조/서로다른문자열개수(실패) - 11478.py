S = input()

words = []

for i in range(1, len(S)+1):
    for j in range(len(S) - i +1):
        word = S[j:j+i]
        if word not in words: # 중복인 경우에는 추가 X
            words.append(word)
        
print(len(words)) # 길이, 내부의 개수를 출력

# 시간초과.
# 1000차이므로 (1+1000)/2 * 1000이므로
# 최악의 경우 500500, 1초 초과. 

'''
1인 경우에는 중복되지 않게 하나씩만 추가한다.
2이상부터는 조합을 생각해야한다. 
이중 for문을 사용해서 풀어보자

a b a b c

0 1 2 3 4
a b a b c
0:1 1:2 2:3 3:4
ab ba ab bc
0:2 1:3 2:4
aba bab abc
0:3 1:4
abab babc
0:4 
ababc

5+4+3+2+1 - 3 중복을 뺸다 
그러면 리스트에 append하고 not in를 사용하면 될거같다.

'''