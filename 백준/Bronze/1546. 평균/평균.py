N = int(input())
num = list(map(int, input().split()))
print(sum(num)/max(num)*100/N)