import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
result = [0] * N
stack = []

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        result[stack.pop()] = A[i]
    stack.append(i)
    
while stack:
    result[stack.pop()] = -1

for i in range(N):
    sys.stdout.write(str(result[i]) + " ")