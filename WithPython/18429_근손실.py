# 백준 18429 근손실 실3

# 하루가 지날때마다 중량이 K만큼 감소.
# N개의 키트 하루에 1개 사용 각각 중량 증가량이 있음
# 항상 500이상이 되도록 유지하기

# 가능한 경우의 수를 출력

# 백트래킹?

N, K = map(int, input().split())

arr = list(map(int, input().split()))
visited = [False for _ in range(N)]

answer = 0

now = 500


def backTrack(back):
    global now
    global answer

    if len(back) == N:
        answer += 1

    for i in range(N):
        if not visited[i]:
            now -= K
            now += arr[i]

            if now >= 500:
                visited[i] = True
                backTrack(back+[i])

            now += K
            now -= arr[i]
            visited[i] = False


backTrack([])

print(answer)
