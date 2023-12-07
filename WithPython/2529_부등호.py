# 백준 2529 부등호 실1

k = int(input())
compares = list(map(str, input().split()))

answer = []


def backTrack():
    l = len(s)
    last = s[-1]

    if len(s) == k+1:
        answer.append(''.join(map(str, s)))
        return

    if compares[l-1] == '>':
        for j in range(0, last):
            if j not in s:
                s.append(j)
                backTrack()
                s.pop()
    else:
        for j in range(last+1, 10):
            if j not in s:
                s.append(j)
                backTrack()
                s.pop()


s = []

for i in range(10):  # 0~9
    s.append(i)
    backTrack()
    s.pop()

print(answer[-1])
print(answer[0])
