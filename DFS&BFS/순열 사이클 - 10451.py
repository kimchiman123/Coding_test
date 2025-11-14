def dfs(node, graph, visited):
    """방문하지 않은 노드를 따라가면서 사이클을 찾는 DFS 함수"""
    visited[node] = True  # 현재 노드를 방문 처리
    next_node = graph[node]  # 다음 이동할 노드
    print(f"방문기록:{visited}")
    print(f"그래프 :{graph}")

    if not visited[next_node]:  # 방문하지 않았다면 계속 탐색
        dfs(next_node, graph, visited)

# 입력 처리
T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    N = int(input())  # 순열 크기
    permutation = list(map(int, input().split()))  # 순열 입력

    # 그래프와 방문 체크 배열 초기화
    graph = [0] + permutation  # 1-based index 사용
    visited = [False] * (N + 1)  
    cycle_count = 0  # 사이클 개수

    for i in range(1, N + 1):
        if not visited[i]:  # 방문하지 않은 노드에서 DFS 시작
            dfs(i, graph, visited)
            cycle_count += 1  # 한 번의 DFS가 끝나면 사이클 하나 찾음

    print(cycle_count)  # 결과 출력
