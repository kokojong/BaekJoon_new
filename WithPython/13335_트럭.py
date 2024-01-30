# 백준 13335 트럭 실1

from collections import deque

N, W, L = map(int, input().split())  # 트럭수, 동시에 트럭수, 하중

arr = list(map(int, input().split()))  # 길이: N

queue = deque(arr)

bridge = deque([0 for _ in range(W)])

# print(bridge)

answer = 0

while True:
    if sum(bridge) == 0 and not queue:
        # 대기중인것도 없고 bridge에 암것도 없다면
        break

    bridge.popleft()

    if queue:
        if sum(bridge) + queue[0] <= L:
            bridge.append(queue.popleft())  # 대기열에서 하나 넣기
        else:
            bridge.append(0)
    else:
        bridge.append(0)

    answer += 1

print(answer)
