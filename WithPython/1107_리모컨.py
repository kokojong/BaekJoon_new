# 백준 1107 리모컨 골5

# from itertools import

N = int(input())
numbers = [i for i in range(10)]

k = int(input())
if k < 1:
    print(len(str(N)))
    exit()

li = list(map(int, input().split()))

now = 100
answer = abs(now - N)

for num in range(1000001):
    num = str(num)

    for i in range(len(num)):
        if int(num[i]) in li:
            break

        else:
            # result = abs(N - int(num)) + len(num)
            answer = min(answer, abs(int(num) - N) + len(num))

print(answer)
