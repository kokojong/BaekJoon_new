# 백준 2792 보석 상자 실1

import math
import sys
input = sys.stdin.readline

# N명에게 나눠줌. M가지 색 보석
# 보석을 받지 못하는 학생이 있어도 되는데 같은 색만 가져가게 된다

# 가장 많은 보석을 가져간 학생이 가진 갯수 - 질투심 -> 이게 최소화
N, M = map(int, input().split())

arr = []

for _ in range(M):
    arr.append(int(input()))

l = 1
r = max(arr)
answer = r

while l <= r:
    mid = (l+r)//2  # 질투심의 최대값

    cnt = 0
    for a in arr:
        cnt += math.ceil(a/mid)  # 최소한 몇명으로 쪼개져야하는지

    # print("mid, cnt", mid, cnt)
    if cnt > N:  # 최대 크기가 mid일때
        l = mid + 1
    else:
        answer = min(answer, mid)
        r = mid-1

print(answer)
