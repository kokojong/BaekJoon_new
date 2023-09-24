# 백준 5430 AC 골5

# R: 뒤집기 - 배열에 있는 수를 뒤집기
# D: 버리기 - 첫번째 수를 버리기. 비어있다면 에러발생

from collections import deque
import sys
input = sys.stdin.readline


T = int(input())

for t in range(T):
    P = str(input())
    l = int(input())
    arr = deque(input().rstrip()[1:-1].split(","))

    # print("arr", arr)
    if l == 0:
        arr = deque()

    rev = 0
    flag = True
    for p in P:
        if p == 'R':  # 매번 뒤집으면 시간초과가 발생
            # arr.reverse()
            rev += 1
        elif p == 'D':
            if len(arr) >= 1:
                if rev % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                flag = False
                print('error')
                break
    if rev % 2 == 1:
        arr.reverse()
    if flag:
        print("[" + ",".join(arr) + "]")
