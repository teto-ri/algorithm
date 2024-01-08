def avg(num):
    return sum(num) / len(num)

N = int(input())
num = list(map(int, input().split()))
maximum = max(num)
num = [i / maximum * 100 for i in num]
print(avg(num))