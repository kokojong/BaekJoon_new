# 백준 15657 N과 M (8) 실3

N, M = map(int, input().split())

# N개의 자연수 중 M개를 고른 수열
# 중복 가능
# 고른 수열은 비 내림차순이어야 함(더 작은걸 고르면 안된다)

arr = list(map(int, input().split()))
arr.sort()


def dfs(s, l):
    if len(s) == l:
        print(' '.join(map(str, s)))

    else:
        for a in arr:
            if s:
                if s[-1] <= a:
                    dfs(s+[a], l)
                else:
                    continue
            else:
                dfs([a], l)


dfs([], M)
