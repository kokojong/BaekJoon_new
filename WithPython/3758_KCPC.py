# 백준 3758 KCPC 실2

from collections import defaultdict

T = int(input())

for _ in range(T):
    n, m, myTeam, l = map(int, input().split())
    # 팀갯수, 문제갯수, 팀 id, 로그 갯수

    # problems[t] 팀이 문제별로 몇점인지
    problems = [defaultdict(int) for _ in range(n+1)]

    arr = [
        [-1, 0, 0, i] for i in range(n+1)  # 총점, 제출횟수, 마지막 제출 시간, index
    ]

    for i in range(l):  # 로그의 순서
        t, p, point = map(int, input().split())
        problems[t][p] = max(problems[t][p], point)  # 더 높은 값으로 갱신
        arr[t][1] += 1  # 제출횟수
        arr[t][2] = i

    # print("problems", problems)
    for t in range(1, n+1):
        score = sum(problems[t].values())
        arr[t][0] = score

    # print("arr", arr)
    arr.sort(key=lambda x: (-x[0], x[1], x[2]))
    # print("sorted", arr)

    for i in range(n):
        if arr[i][3] == myTeam:
            print(i+1)
            break
