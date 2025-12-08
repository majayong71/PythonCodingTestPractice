from collections import deque

# ============= 1. 입력 & 초기화 =============
def solution3():
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    for i in range(1, n + 1):
        graph[i].sort()


# ============= 2. 그래프 생성 =============


# ============= 3. 간선 연결 =============


# ============= 4. 정렬 (문제 조건에 따라) =============


# ============= 5. DFS 템플릿 =============


# ============= 6. BFS 템플릿 =============


# =============7. 출력 =============




def solution():
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1 , n + 1 ):
        graph[i].sort()

    def dfs(start): # v로 해도 되지만 가독성으로 start 라 적었을 때 더 알아보기 직관적이기 때문에 start 라 하고 호출할 때 v로 호출한다.
        visited = [False] * (n + 1)
        result = []

        def dfs_recursive(node): # node : 현재 방문 중인 노드
            visited[node] = True
            result.append(node)

            for neighbor in graph[node]: # neighbor : 현재 노드와 인접한 노드
                if not visited[neighbor]: # 방문하지 않은 ( True 가 아닌 ) 경우에는
                    dfs_recursive(neighbor) # 재귀적으로 dfs_recursive 호출

        dfs_recursive(start) # start 를 첫 노드로 전달
        return result

    def bfs(start):
        visited = [False] * (n + 1)
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
    dfs_result = dfs(v)
    bfs_result = bfs(v)

    print(' '.join(map(str, dfs_result)))
    print(' '.join(map(str, bfs_result)))

if __name__ == '__main__':
    solution()