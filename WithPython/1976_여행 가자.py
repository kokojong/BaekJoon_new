# 백준 1976 여행 가자 골4

N = int(input())

M = int(input())

parents = [i for i in range(N)]


def findParent(x):
    if parents[x] != x:
        parents[x] = findParent(parents[x])
    return parents[x]


for i in range(N):
    row = list(map(int, input().split()))

    for j in range(N):
        if row[j]:
            A = findParent(i)
            B = findParent(j)

            if A < B:
                parents[B] = A
            else:
                parents[A] = B

travels = list(map(int, input().split()))
# parents = [-1] + parents

start = travels[0] - 1  # k번째 -> k-1
for i in range(1, M):
    next = travels[i] - 1
    if findParent(start) != findParent(next):
        print("NO")
        exit()
print("YES")
