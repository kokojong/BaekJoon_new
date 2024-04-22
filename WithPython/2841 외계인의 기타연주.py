# 백준 2841 외계인의 기타연주 실1
import sys
input = sys.stdin.readline

N, P = map(int, input().split())

# 6개의 줄은 기본.

# 한 줄당 최대 P까지 가능하다!

stacks = [[] for _ in range(7)]  # 1~6번 쓰려고

answer = 0

for _ in range(N):
    n, p = map(int, input().split())

    # print(stacks[n], answer)
    if stacks[n] == []:
        stacks[n].append(p)
        answer += 1
    else:
        if stacks[n][-1] < p:
            stacks[n].append(p)
            answer += 1
        elif stacks[n][-1] == p:
            continue
        else:
            while stacks[n] and stacks[n][-1] > p:
                stacks[n].pop()
                answer += 1
            if stacks[n] and stacks[n][-1] == p:
                continue
            stacks[n].append(p)
            answer += 1
    # print(answer)

print(answer)
