# 백준 2023 신기한 소수 골5

import math

N = int(input())

# isSosu = [True for _ in range(10**N)]  # 4 -> 1000 ~ 9999
# M = 10**N-1

# isSosu[0] = False
# isSosu[1] = False

# for i in range(2, int(math.sqrt(M))+1):
#     for j in range(2, M//i + 1):
#         isSosu[i * j] = False


def isSosu(x):
    if x < 2:
        return False

    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


def backTrack(depth):
    if depth == N:
        print(''.join(map(str, num)))
        return

    for i in [1, 3, 7, 9]:  # 뒤에 붙을수 있는것
        k = int(''.join(map(str, num+[i])))
        # print("k", k)
        if isSosu(k):
            num.append(i)
            backTrack(depth + 1)
            num.pop()


for i in [2, 3, 5, 7]:
    num = [i]
    backTrack(1)
