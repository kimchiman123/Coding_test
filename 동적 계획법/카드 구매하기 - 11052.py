def card_price(array, n):
    dp = [0] * (n+1) 
    for i in range(1, n+1): # 카드의 개수
        for j in range(1, i+1): # 사용할 카드팩
            dp[i] = max(dp[i], dp[i-j] + array[j])
            print(f"{i}번쨰: {dp[i]}")

    return dp[n]

n = int(input())
cards_value = [0] + list(map(int, input().split()))

print(card_price(cards_value, n))
