# 백준 1911 흙길 보수하기 골5

import sys
input = sys.stdin.readline

N, L = map(int, input().split())

water = []
for _ in range(N):
    s, e = map(int, input().split())
    water.append([s, e])
# print(end)

water.sort()

answer = 0
last = -1  # 널판지의 마지막 끝점?
for s, e in water:

    if s > last:  # 새로 깔아야함
        # print("case 1")
        cnt = (e-s-1)//L + 1  # 1~6 -> 2개가 들어가야함
        last = s + cnt * L - 1
        answer += cnt
        # print("s, e, last, cnt", s, e, last, cnt)
        continue

    else:
        # print("case 2")
        s = last + 1
        cnt = (e-s-1)//L + 1
        last = s + cnt * L - 1
        answer += cnt
        # print("s, e, last, cnt", s, e, last, cnt)
        continue
print(answer)
