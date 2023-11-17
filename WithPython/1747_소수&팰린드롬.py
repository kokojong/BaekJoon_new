# 백준 1747 소수&팰린드롬 실1

import math

N = int(input())
K = 10**6 * 2

sosu = [True for _ in range(K+1)]  # 0 ~ N까지의 소수 여부
sosu[0] = False
sosu[1] = False
for i in range(2, int(math.sqrt(K))+1):
    for j in range(2, K//i + 1):
        sosu[i * j] = False


def check(x):
    xx = int(''.join(list(str(x))[::-1]))
    return x == xx


for i in range(N, K+1):
    if sosu[i] and check(i):
        print(i)
        break
