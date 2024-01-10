# 백준 2607 비슷한 단어 실2

N = int(input())

t = list(input().rstrip())

answer = 0

for _ in range(N-1):
    target = t[:]
    word = list(input().rstrip())
    cnt = 0

    for w in word:
        if w in target:
            target.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(target) < 2:
        answer += 1

print(answer)
