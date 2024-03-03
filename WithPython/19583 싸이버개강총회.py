# 백준 19583 싸이버개강총회 실2

# 시작전에 입장 확인. (시작 이전에 대화, 시작하자마자 채팅도 ㅇㅈ)
# 끝나고나서 퇴장 확인 여부. 개총 끝나고 스트리밍 존료까지 대화.(개총or스트리밍이 끝나자마자 채팅 했어요 퇴장 ㅇㅈ)

from collections import defaultdict
import sys

input = sys.stdin.readline


def ToInt(s):
    h, m = map(int, s.split(':'))
    time = h * 60 + m

    return time


S, E, Q = map(str, input().split())
S = ToInt(S)
E = ToInt(E)
Q = ToInt(Q)

# print(S, E, Q)

dic = defaultdict(int)

answer = 0

while True:
    try:
        t, name = input().split()
        t = ToInt(t)
        # print("t, name", t, name)

        if t <= S:
            dic[name] = 1
        elif E <= t <= Q and dic[name] == 1:
            dic[name] += 1
            answer += 1
    except:
        # print("끝")
        break

print(answer)
