from collections import deque
N, M, V = map(int, input().split())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)
    
for i in range(N+1):
    A[i].sort()

def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)
DFS(V)
print()

def BFS(v):
    queue = deque([v])
    visited = [False] * (N+1)
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in A[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
BFS(V)            
