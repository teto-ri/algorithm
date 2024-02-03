import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
dfs = [0] * (n+1)

def DFS(v):
    dfs[v] = 1
    for i in A[v]:
        if dfs[i] == 0:
            DFS(i)

for _ in range(m):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)
    
cnt = 0

for i in range(1, n+1):
    if dfs[i] == 0:
        DFS(i)
        cnt += 1
print(cnt)