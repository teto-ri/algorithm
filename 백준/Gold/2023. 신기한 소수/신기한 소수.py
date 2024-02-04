import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

N = int(input())

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def DFS(n):
    if len(str(n)) == N:
        print(n)
        return
    for i in range(1, 10, 2):
        if isPrime(n * 10 + i):
            DFS(n * 10 + i)
            
DFS(2)
DFS(3)
DFS(5)
DFS(7)
