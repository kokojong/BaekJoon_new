# 백준 15654 N과 M (5) 실3

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()


def dfs(s, l):
    if len(s) == l:
        print(' '.join(map(str, s)))

    else:
        for a in arr:
            if a not in s:
                dfs(s + [a], l)


dfs([], M)
