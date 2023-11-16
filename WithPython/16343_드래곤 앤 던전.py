# 백준 16343 드래곤 앤 던전 골4

import math
import sys
input = sys.stdin.readline

N, ATK = map(int, input().split())

arr = []
for _ in range(N):
    # t가 1이면 -> a가 공격력, h가 생명력인 몬스터 t가 2이면 공격력이 a만큼 증가, 체력 h만큼 증가
    t, a, h = map(int, input().split())
    arr.append((t, a, h))


def check(atk, maxH):
    nowH = maxH

    for t, a, h in arr:
        if t == 1:
            turn = math.ceil(h/atk)
            nowH -= (a * (turn-1))

            # h -= atk  # 공격
            # if h <= 0:
            #     break
            # nowH -= a
            # if nowH <= 0:
            #     return False
        elif t == 2:
            atk += a
            nowH = min(nowH + h, maxH)

        if nowH <= 0:
            return False

    return True


left = 1
right = N * (10**6) * (10**6)  # 공격력 1일때 체력 최대로(나랑 몬스터 둘다 최대)
answer = right

while left <= right:
    mid = (left + right) // 2

    if check(ATK, mid):
        right = mid-1
        answer = min(answer, mid)
    else:
        left = mid + 1

print(answer)
