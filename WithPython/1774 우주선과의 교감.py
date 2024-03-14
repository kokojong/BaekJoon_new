# 백준 1774 우주와의 교감 골3

N, M = map(int, input().split())  # 우주신 개수, 통로 개수


def distance(p1, p2):
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


def findParent(x):
    if parents[x] != x:
        parents[x] = findParent(parents[x])

    return parents[x]


def union(a, b):
    pA = findParent(a)
    pB = findParent(b)
    # print("pA, pB", pA, pB)

    if pA == pB:
        return

    if pA < pB:
        parents[pB] = pA
    else:
        parents[pA] = pB

    # print("parents", parents)


stars = [[]]
graph = [[] for _ in range(N+1)]
parents = [i for i in range(N+1)]

for _ in range(N):
    x, y = map(int, input().split())
    stars.append((x, y))

for _ in range(M):  # 이미 이어진 애들
    a, b = map(int, input().split())  # a랑 b랑 연결
    union(a, b)

# print(parents)
lines = []
for i in range(1, N+1):
    for j in range(1, N+1):
        c = distance(stars[i], stars[j])
        lines.append((c, i, j))

lines.sort()  # 가장 거리 짧은것 부터 정렬

# print("lines", lines)

answer = 0

for l in lines:
    c, a, b = l
    pA = findParent(a)
    pB = findParent(b)

    if pA != pB:  # 같은 부모가 아니라면
        union(a, b)
        # print("a, b 합친 결과", a, b, c, parents)
        answer += c
# print(parents)
# print(answer)
print("{:.2f}".format(answer))
