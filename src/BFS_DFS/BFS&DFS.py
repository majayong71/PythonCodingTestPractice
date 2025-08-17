"""
DFS와 BFS
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	338280	136467	80544	38.869%
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단,
방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예제 입력 1

4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1

1 2 4 3
1 2 3 4
예제 입력 2

5 5 3
5 4
5 2
1 2
3 4
3 1
예제 출력 2
3 1 2 5 4
3 1 4 2 5
예제 입력 3
1000 1 1000
999 1000
예제 출력 3
1000 999
1000 999
"""

from collections import deque

def solve_dfs_bfs():
    # 1. 입력받기
    n, m, v = map(int, input().split()) # 정점 , 간선 , 시작점

    # 2. 그래프 생성 (인접 리스트)  2차원 배열 생성과정
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):             # 입력받은 m 만큼 반복 (간선)
        a, b = map(int, input().split()) # 간선 연결 과정
        graph[a].append(b)
        graph[b].append(a)

    # 3. 정점 번호가 작은 것부터 방문하기 위해 정렬
    for i in range(1, n + 1):
        graph[i].sort()

    # 4. DFS 구현        재귀 or  stack 스택 # start , node 는 call stack 이다
    def dfs(start):
        visited = [False] * (n + 1) # 방문 체크 배열
        result = []                 # 방문 순서 저장

        def dfs_recursive(node):      # 재귀 함수
            visited[node] = True      # 현재 노드 방문 표시
            result.append(node)       # 결과에 추가

            for neighbor in graph[node]:  # 인접한 모든 노드 확인
                if not visited[neighbor]: # 아직 방문 안 한 노드라면
                    dfs_recursive(neighbor) # 재귀 호출로 깊이 탐색

        dfs_recursive(start)
        return result

    # -------------------------------------------------

    # 5. BFS 구현
    def bfs(start):
        visited = [False] * (n +1)
        queue = deque([start])
        visited[start] = True
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return result

    # 6. 결과 출력
    dfs_result = dfs(v)
    bfs_result = bfs(v)

    print(''.join(map(str, dfs_result)))
    print(''.join(map(str, bfs_result)))

# 함수 실행
solve_dfs_bfs()