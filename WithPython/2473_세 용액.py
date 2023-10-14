# 백준 2473 세 용액 골3

# 산성 1~10억, 알칼리 -1~-10억
# 세가지 용액을 혼합한 특성값 -> 합으로 정의
# 0에 가까운 용액 만들기

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = float('INF')  # 0에 가깝게 만들기

answer = []

for l in range(N-2):  # 맨 왼쪽 고정
    m = l+1
    r = N-1

    while m < r:
        total = arr[l] + arr[m] + arr[r]

        if abs(total) < abs(result):

            result = abs(total)
            answer = [arr[l], arr[m], arr[r]]

        if total < 0:
            m += 1
        elif total > 0:
            r -= 1
        else:  # 0과 동일한 경우
            print(" ".join(map(str, answer)))
            exit()

print(" ".join(map(str, answer)))
