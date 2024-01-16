# 백준 13913 숨바꼭질 4 골4

# 현재 N, 동생은 K

# 1초후 -1 or +1 또는 2배로 이동

# 가장 빠른 시간, 어떻게 이동하는지 기록하기

from collections import deque

N, K = map(int, input().split())

# 각각을 배열로 가지고 있기 -> false로 바꿔주고 queue에만 배열 넣기
visited = [False for _ in range(200001)]

queue = deque()
queue.append((N, [N]))
visited[N] = True

# 시간 줄이기 최적화
if N > K:
    print(N - K)
    print(*[x for x in range(N, K-1, -1)])
    exit()

while queue:
    q, arr = queue.popleft()
    if q == K:
        print(len(arr) - 1)
        print(*arr)
        exit()

    for i in [-1, 1, q]:
        qq = q + i
        # print("qq", qq, visited[qq])
        if qq > 200000 or qq < 0 or visited[qq]:
            continue

        visited[qq] = True
        queue.append((qq, arr + [qq]))
