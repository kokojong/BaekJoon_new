# 백준 11657 타임머신 골4

N, M = map(int, input().split())

# INF = 500 * 10000
INF = float('inf')

edges = []

for _ in range(M):
    s, e, t = map(int, input().split())
    edges.append((s, e, t))

distances = [INF for _ in range(N+1)]


def belman(start):
    distances[start] = 0

    for i in range(N):
        for s, e, t in edges:
            if distances[s] != INF and distances[s] + t < distances[e]:
                distances[e] = distances[s] + t

                if i == N-1:  # 마지막인데도 갱신이 가능하면 -> 음수 루프
                    return False
    return True


result = belman(1)
# print("dis", distances)
if result:
    for i in range(2, N+1):
        if distances[i] != INF:
            print(distances[i])
        else:
            print(-1)
else:
    print(-1)
