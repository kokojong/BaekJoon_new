from collections import deque

N, M = map(int, input().split(' '))

# 1부터 N+1 까지 직접 bfs로 걸리는 시간을 각각 구함

arr = [[0 for _ in range(N+1)] for _ in range(N+1)]

for m in range(M):
    a, b = map(int, input().split(' '))
    arr[a][b] = 1
    arr[b][a] = 1

answer = []

for k in range(1, N+1):  # 중간
    for i in range(1, N+1):  # 시작
        for j in range(1, N+1):  # 끝
            if i == j:
                continue

            if arr[i][k] and arr[k][j]:  # 연결이 가능하다면
                if arr[i][j] == 0:  # 연결이 안되어있다면
                    arr[i][j] = arr[i][k] + arr[k][j]

                else:
                    # graph[j][k] = min(graph[j][k],graph[j][i] + graph[i][k])
                    arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

# print(arr)

for a in arr:
    answer.append(sum(a))
answer.pop(0)

minV = min(answer)
for v in enumerate(answer):
    if v[1] == minV:
        print(v[0]+1)
        break

# 5 5
# 1 3
# 1 4
# 4 5
# 4 3
# 3 2
