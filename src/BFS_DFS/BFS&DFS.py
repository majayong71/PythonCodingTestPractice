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
    for i in range(1, n + 1):    # graph[] 를 1부터 n+1 까지 정렬하기위해 range(1, n + 1) 을 i에 대입하며 n+1 까지 반복한다
        graph[i].sort()

        """
        n m v 를 입력받고,
        n, m, v = map(int, input().split())

        그래프를 생성한다
        graph = [[] for _ in range(n +1)]
        이렇게 해줘야

        [], 0번
        [2, 3, 4], 1번 -> 여러 정점과 연결
        [], 2번
        [], 3번
        표현이 가능해지기 때문이다.

        입력받은 m 만큼 반복되는 간선 연결 과정을 만들고
        for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        [] [] [] [] []  가 있으면
        첫번째 두번째 세번째 네번째 다섯번쨰
        첫번째 graph[a] 에 append(b) 를 넣는다
        그럼 [] [b] [] [] [] 이렇게    되고
        두번째 graph[b] 에 append(a) 를 넣는다
        그럼 [] [b] [a] [] [] 이렇게 된다.

        정점 번호가 작은것부터 방문하기 위해 정렬하고

        DFS 를 구현한다 재귀 or stack 으로
        """

    # 4. DFS 구현        재귀 or  stack 스택 # start , node 는 call stack 이다
    def dfs(start):     # start 는 시작지점을 지정하는 파라미터이다.
        visited = [False] * (n + 1) # 방문 체크 배열 (1차원 배열)
        result = []                 # 방문 순서 저장

        def dfs_recursive(node):      # 재귀 함수
            visited[node] = True      # 현재 노드 방문 표시
            result.append(node)       # 결과에 추가ㄱ

            for neighbor in graph[node]:  # 인접한 모든 노드 확인 ex) graph[1] = [2, 3, 4]
                                          # neighbor 는 graph[node] 에서 하나씩 꺼내는 역할 2가 됐다가 3,4가 되는것이다.
                if not visited[neighbor]: # 아직 방문 안 한 노드라면
                    dfs_recursive(neighbor) # 재귀 호출로 깊이 탐색

        dfs_recursive(start)
        return result

    # -------------------------------------------------

    # 5. BFS 구현
    def bfs(start):
        visited = [False] * (n +1) # 똑같이 방문 체크 배열을 만들어준다 ( 1차원 배열 )
        queue = deque([start])     # deque([start]) 시작점부터 진행한다는 뜻.
        visited[start] = True
        result = []

        while queue:               # queue 에 값이 있는 동안에 반복하는 구문 (값이 있으면 True, 없으면 False , False 일 때 종료)
            node = queue.popleft() # queue에 들어있는 값을 빼서 node 에 저장한다
                                   # ex) # 예시: queue = deque([1, 2, 3])
                                   # node = queue.popleft()  # 맨 앞의 1을 꺼냄
                                   # 결과: node = 1, queue = deque([2, 3])
            result.append(node)    # node 에 임시적으로 저장된 값들을 result 에 저장

            for neighbor in graph[node]:  # 현재 노드와 연결된 모든 이웃들을 하나씩 확인해서,
                if not visited[neighbor]: # 아직 방문하지 않은 이웃을 큐에 예약한다.
                    visited[neighbor] = True # 방문표시를 true 로 변경하고
                    queue.append(neighbor) # 이웃값을 queue 에 추가

        return result

    # 6. 결과 출력
    dfs_result = dfs(v)
    bfs_result = bfs(v)

    print(''.join(map(str, dfs_result)))
    print(''.join(map(str, bfs_result)))


# 함수 실행
solve_dfs_bfs()

# """ 답안지 """
# from collections import deque
#
#
# def solve_dfs_bfs():
#     n, m, v = map(int, input().split())
#
#     graph = [[] for _ in range(n + 1)]
#
#     for _ in range(m):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         graph[b].append(a)
#
#     for i in range(1, n + 1):
#         graph[i].sort()
#
#     def dfs(start):
#         visited = [False] * (n + 1)
#         result = []
#
#         def dfs_recursive(node):
#             visited[node] = True
#             result.append(node)
#
#             for neighbor in graph[node]:
#                 if not visited[neighbor]:
#                     dfs_recursive(neighbor)
#
#         dfs_recursive(start)
#         return result
#
#     def bfs(start):  # ✅ 올바른 들여쓰기!
#         visited = [False] * (n + 1)
#         queue = deque([start])
#         visited[start] = True
#         result = []
#
#         while queue:
#             node = queue.popleft()
#             result.append(node)
#
#             for neighbor in graph[node]:
#                 if not visited[neighbor]:
#                     visited[neighbor] = True
#                     queue.append(neighbor)
#
#         return result
#
#     # ✅ 함수 호출과 출력 추가!
#     dfs_result = dfs(v)
#     bfs_result = bfs(v)
#
#     print(' '.join(map(str, dfs_result)))  # ✅ 공백으로 구분!
#     print(' '.join(map(str, bfs_result)))
#
#
# if __name__ == '__main__':
#     solve_dfs_bfs()