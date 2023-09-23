# 백준 24856 나는 정말 휘파람을 못 불어 골4

import sys
input = sys.stdin.readline

N = int(input())
arr = list(input())

wSum = [0 for _ in range(N)]
hSum = []  # h 가 기준이니까
eSum = [0 for _ in range(N)]

mod = 10**9 + 7
# idea: w h ee가 나와야하니까 h가 등장한 시점 기준으로 왼쪽에서 W를 1개 선택, 오른쪽에서 e를 2개이상 선택

answer = 0

w = 0
e = 0

for i in range(N):
    if arr[i] == 'W':
        w += 1

    elif arr[i] == 'E':
        e += 1

    elif arr[i] == 'H':
        hSum.append(i)

    wSum[i] = w
    eSum[i] = e


# print(wSum)
# print(eSum)
# print(hSum)

# twoes = [1 for _ in range(N+1)]  # 2**n을 하는데 사용...?
# for i in range(1, N+1):
#     twoes[i] = twoes[i-1] * 2
#     twoes[i] %= mod

for h in hSum:
    ww = wSum[h]
    ee = eSum[-1] - eSum[h]
    # result = (2 ** ee - ee - 1) % mod
    # result = (twoes[ee] - ee - 1) % mod
    # result *= ww

    result = ww * (2**ee - ee - 1) % mod  # 여기서 e를 2개이상 뽑는 횟수
    # result %= mod

    answer += result
    answer %= mod

print(answer)
