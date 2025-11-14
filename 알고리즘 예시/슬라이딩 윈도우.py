def max_sum_sliding_window(arr, k):
    max_sum = float('-inf')
    window_sum = sum(arr[:k])  # 첫 번째 윈도우 합
    max_sum = window_sum

    for i in range(len(arr) - k):
        print(f"{i}: i, {k}: k")
        window_sum += arr[i + k] - arr[i]  # 윈도우를 이동하면서 합 조정
        max_sum = max(max_sum, window_sum)

    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_sliding_window(arr, k))  # 출력: 9
