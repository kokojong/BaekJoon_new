# 백준 2805 나무 자르기 실2

N, M = map(int, input().split())  # 나무수, 가져가려는 나무의 길이

arr = list(map(int, input().split()))

m = max(arr)

l = 0
r = m
while l <= r:
    mid = (l+r)//2

    cnt = 0
    for a in arr:
        if a > mid:
            cnt += (a-mid)

    if cnt >= M:
        answer = mid
        l = mid + 1
        # print("answer", answer)
    else:
        r = mid - 1

print(answer)
