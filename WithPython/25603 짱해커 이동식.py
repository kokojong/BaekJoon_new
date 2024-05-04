# 백준 25603 짱해커 이동식 골5

# 최대한 비용이 적게 들게
# 연속으로 K번 개중에서 최소 1개는 해야함
# 수락한 애들중에서 가장 높은 비용인거 확인

N, K = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0  # 최대 비용
now = 0  # 마지막으로 받은 의뢰의 다음 index

while now+K <= N:
    window = arr[now:now+K]
    minV = min(window)

    for i in range(now+K-1, now-1, -1):
        if arr[i] == minV:
            now = i + 1  # 선택한거 다음으로 갱신해야해서
            break

    answer = max(minV, answer)

print(answer)
