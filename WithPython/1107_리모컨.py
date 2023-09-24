# 백준 1107 리모컨 골5

# from itertools import

N = int(input())
numbers = [i for i in range(10)]

_ = int(input())
li = list(map(int, input().split()))

now = 100
answer = abs(now - N)

for num in range(0, 1000001):
    num = str(num)

    for i in range(len(num)):
        if int(num[i]) in li:
            break

        elif i == len(num) - 1:
            result = abs(N - int(num)) + len(num)

            if result < answer:
                answer = result

print(answer)
