import sys
input = sys.stdin.readline

N = int(input())
n = [int(input()) for _ in range(N)]
n.sort()

for i in n:
    print(i)