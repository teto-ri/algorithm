import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

N,M = map(int,input().split())
arrive = 0
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def DFS(n,depth):
    global arrive
    if depth == 5:
        arrive = 1
        return
    visited[n] = True
    for i in A[n]:
        if not visited[i]:
            DFS(i,depth+1)
    visited[n] = False

for i in range(M):
    a,b = map(int,input().split())
    A[a].append(b)
    A[b].append(a)
    
for i in range(N):
    DFS(i,1)
    if arrive:
        break
if arrive:
    print(1)
else:
    print(0)