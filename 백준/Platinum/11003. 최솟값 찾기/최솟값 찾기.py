from collections import deque
N, L = map(int, input().split())
A = list(map(int, input().split()))
window = deque()

for i in range(N):
    while window and window[-1] > A[i]:
        window.pop()
    window.append(A[i])
    if i >= L and window[0] == A[i - L]:
        window.popleft()
    print(window[0], end=' ')