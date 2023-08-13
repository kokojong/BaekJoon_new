n = int(input())
m = int(input())

parents = [i for i in range(n+1)]  # 각각의 부모를 저장


def findParent(parents, a):
    if parents[a] != a:
        parents[a] = findParent(parents, parents[a])

    return parents[a]


def union(parents, a, b):
    parentA = findParent(parents, a)
    parentB = findParent(parents, b)

    if parentA < parentB:
        # 실수한 부분: parents[b] = parentA 라고 씀 ㅡㅡ 지피티는 이걸 못찾음
        parents[parentB] = parentA
    else:
        parents[parentA] = parentB


for _ in range(m):
    a, b = map(int, input().split())
    union(parents, a, b)

answer = 0

for p in range(1, n+1):
    if findParent(parents, p) == 1:
        answer += 1

print(answer - 1)


# def find(parent, x):
#     if parent[x] != x:
#         parent[x] = find(parent, parent[x])
#     return parent[x]

# def union(parent, a, b):
#     a = find(parent, a)
#     b = find(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b


# n = int(input())
# v = int(input())
# parent = [i for i in range(n + 1)]

# for _ in range(v):
#     a, b = map(int, input().split())
#     union(parent, a, b)

# answer = 0
# for i in range(1, n+1):
#     if find(parent, i) == 1:
#         answer += 1

# print(answer-1)
