# 백준 1038 감소하는 수 골5

import sys
input = sys.stdin.readline

# 최대 가능한건 98 7654 3210 -> 너무 큰수라서 시간초과가 날거임
N = int(input())

answers = []
arr = []


def backTrack():
    global arr

    for i in range(10):
        arr.append(i)

        if len(arr) == 1:
            backTrack()
            # arr.append(int(''.join()))
            s = ''.join(str(n) for n in arr)
            answers.append(int(s))

        elif len(arr) > 1 and arr[-2] > i:
            backTrack()
            s = ''.join(str(n) for n in arr)
            answers.append(int(s))

        arr.pop()


backTrack()
answers.sort()
if N < len(answers):
    print(answers[N])
else:
    print(-1)
