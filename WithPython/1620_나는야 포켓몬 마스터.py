import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dic = dict()
for n in range(1, N+1):
    name = input().rstrip()
    dic[name] = n
    dic[n] = name

for _ in range(M):
    k = input().rstrip()
    if k.isdigit():
        print(dic[int(k)])
    else:
        print(dic[k])
