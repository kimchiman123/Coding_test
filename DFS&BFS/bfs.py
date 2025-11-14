from collections import deque # 큐 구현 

graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D', 'E'],
    'C' : ['A', 'F'],
    'D' : ['B'],
    'E' : ['B', 'F'],
    'F' : ['C' , 'E'],
}

def dfs(graph, start):
    visited = set()            # 방문한 노드를 저장할 집합(중복 방지, O(1) 조회)
    order = []                 # 방문 순서를 기록할 리스트
    stack = [start]            # LIFO 구조의 스택에 시작 노드를 넣고 시작

    while stack:               # 스택이 빌 때까지 반복
        node = stack.pop()     # 스택의 맨 위(마지막)에 있는 노드를 꺼냄
        if node in visited:    # 이미 방문했다면
            continue           # 아래 로직을 건너뛰고 다음 반복으로
        visited.add(node)      # 현재 노드를 방문 처리
        order.append(node)     # 방문 순서에 현재 노드를 추가

        # 인접 노드를 스택에 푸시
        for nei in reversed(graph.get(node, [])):  # 인접 노드 목록이 없을 수도 있어 get 사용
            if nei not in visited:   # 아직 방문하지 않았다면
                stack.append(nei)    # 스택에 추가(나중에 방문)
    return order                    # 전체 방문 순서를 반환