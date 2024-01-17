# 백준 15663 N과 M 9 실2

# N개의 자연수 중에서 M개를 고른 수열

# 중복되는 수열은 X, 사전순으로 증가하는 순서로 출력하기

N, M = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

visited = [False for _ in range(N)]  # 각 숫자별로 visited 처리


def dfs(s):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    flag = 0
    for i in range(N):
        if not visited[i] and flag != arr[i]:
            visited[i] = True
            flag = arr[i]
            dfs(s + [arr[i]])
            visited[i] = False


dfs([])
