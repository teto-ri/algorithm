from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N,M = map(int, input().split())
A = [[0]*M for _ in range(N)]
visit = [[0]*M for _ in range(N)]

for i in range(N):
    num = list(input())
    for j in range(M):
        A[i][j] = int(num[j])

def BFS(i,j):
    q = deque()
    q.append((i,j))
    visit[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if A[nx][ny] == 1 and visit[nx][ny] == 0:
                    q.append((nx,ny))
                    visit[nx][ny] = 1
                    A[nx][ny] = A[x][y] + 1
BFS(0,0)
print(A[N-1][M-1])
