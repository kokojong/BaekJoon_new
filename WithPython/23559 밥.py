# 백준 23559 밥 골5

# 5000원, 1000원

# N일동안 밥먹기, 각 메뉴별 수치를 정해둠.
# 총 X원 이하를 써야함

import heapq

N, X = map(int, input().split())

arr = []

result = 0

heap = []

for _ in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])  # 5000원, 1000원
    result += b
    X -= 1000
    if a > b:  # 만약에 b의 가치가 더 크다면 오히려 손해
        heapq.heappush(heap, -(a - b))  # 뺀 가치가 가장 큰 것 부터 고르기 -> -로 넣어주기

# 일단은 다 1000원으로 고름 -> 금액이 남는 만큼 A에서 고를수 있는데 이 때 가격 대비 가장 괜찮은 것을 고름

# print(X, result)
# print(heap)
# 가능한 갯수 -> X / 4000
x = X // 4000

while x > 0 and heap:
    h = heapq.heappop(heap)
    # print("h", h)
    result -= h
    x -= 1

print(result)
