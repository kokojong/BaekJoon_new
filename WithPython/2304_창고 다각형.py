# 백준 2304 창고 다각형 실2

N = int(input())

arr = []

maxL = 0
maxH = 0

for _ in range(N):
    L, H = map(int, input().split())
    if H > maxH:
        maxH = H
        maxL = L
    arr.append((L, H))

arr.sort()
answer = 0

# 가장 큰 기둥을 중심으로 왼쪽부터 체크

l = arr[0][0]
h = arr[0][1]

for L, H in arr:
    if H > h:  # 지금까지 최대 높이로 면적 계산
        area = (L-l) * h
        answer += area
        # print("area:", area)
        h = H
        l = L

    if H == maxH:
        leftEnd = L
        break

# 오른쪽부터 체크

l = arr[-1][0]
h = arr[-1][1]

for L, H in reversed(arr):
    if H > h:
        area = (l-L) * h
        answer += area
        h = H
        l = L

    if H == maxH:
        RightEnd = L
        break

# 중간에 maxH 만큼의 기둥 처리

answer += (RightEnd - leftEnd + 1) * maxH

print(answer)
