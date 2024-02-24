# 백준 12933 오리 실2

# quack

quack = 'quack'

arr = list(input())
N = len(arr)
visited = [False for _ in range(N)]

answer = 0

if len(arr) % 5 != 0:
    print(-1)
    exit()


def check(start):
    global answer

    isFirst = True
    j = 0  # quack의 현재 index
    for i in range(start, N):
        if arr[i] == quack[j] and not visited[i]:
            visited[i] = True
            if arr[i] == 'k':  # 끝난거면
                if isFirst:
                    answer += 1
                    isFirst = False
                j = 0
                continue

            j += 1


for i in range(N):
    if arr[i] == 'q' and not visited[i]:
        check(i)

if answer == 0 or not all(visited):
    print(-1)
else:
    print(answer)
