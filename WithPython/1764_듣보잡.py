N, M = map(int, input().split())

listen = set()
see = set()

for _ in range(N):
    listen.add(input())

for _ in range(M):
    see.add(input())

answer = sorted(list(listen.intersection(see)))

print(len(answer))
for a in answer:
    print(a)
