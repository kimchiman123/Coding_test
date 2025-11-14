from collections import deque
import sys

dq = deque()
n = int(sys.stdin.readline().strip())  # 빠른 입력 사용
result = []

for _ in range(n):
    user_input = sys.stdin.readline().strip().split()
    
    if len(user_input) == 2:
        command, value = user_input
        value = int(value)  # 정수로 변환
    else:
        command = user_input[0]

    if command == "push_front":
        dq.appendleft(value)
    elif command == "push_back":
        dq.append(value)
    elif command == "pop_front":
        result.append(dq.popleft() if dq else -1)
    elif command == "pop_back":
        result.append(dq.pop() if dq else -1)
    elif command == "size":
        result.append(len(dq))
    elif command == "empty":
        result.append(0 if len(dq) else 1)
    elif command == "front":
        result.append(dq[0] if dq else -1)
    elif command == "back":
        result.append(dq[-1] if dq else -1)

for item in result:
    print(item)
