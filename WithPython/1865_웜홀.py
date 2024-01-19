# 백준 1865 웜홀 골3

# N개의 지점, M개의 도로, W개의 웜홀
# 도로는 방향없고 웜홀만 방향 존재. - 웜홀은 음수

# 한 지점에서 출발해서 다시 출발 위치로 돌아왔을 때 시간이 돌아가있는 경우가 있는지

TC = int(input())

INF = 10001  # 이게 문제였다...! inf - cost = inf가 되는 문제가 발생함


def belman():
    distances = [INF for _ in range(N+1)]  # 이동거리
    # print(edges)

    distances[1] = 0

    for n in range(N):
        for edge in edges:  # 모든 간선을 다 체크
            s = edge[0]
            e = edge[1]
            t = edge[2]

            # distances[s] != INF 조건이 있으면 틀리다고 나옴
            if distances[s] + t < distances[e]:  # 갱신 가능
                distances[e] = distances[s] + t

                # N번 돌렸는데 이때도 갱신이 발생한다면 음의 싸이클이 존재함
                if n == N - 1:
                    return "YES"
    return "NO"


for _ in range(TC):
    N, M, W = map(int, input().split())

    edges = []
    for _ in range(M):
        S, E, T = map(int, input().split())

        edges.append((S, E, T))
        edges.append((E, S, T))

    for _ in range(W):
        S, E, T = map(int, input().split())

        edges.append((S, E, -T))

    print(belman())
