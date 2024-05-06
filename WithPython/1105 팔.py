# 백준 1105 팔 실1

L, R = map(str, input().split())
# L = L.zfill(len(R))

if len(L) != len(R):
    print(0)
    exit()

answer = 0
for i in range(len(R)):
    l = L[i]
    r = R[i]

    if l == r:
        if l == '8':
            answer += 1
    else:
        break
print(answer)
