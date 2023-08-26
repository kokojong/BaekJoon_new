# 백준 11052 카드 구매하기 실1

# 카드 등급은 총 8가지
# Pi 에는 i개의 카드가 들어있다. 그 가격은 Pi이다

# ex) P1 = 1, P2 = 5, P3 = 6, P4 = 7인 경우 4개를 가지고 싶다면 P2를 2개사서 처리

# idea: 각각의 갯수당 가성비를 구하고 그게 제일 큰거 먼저 최대한 소진시키기, 나머지는 또 같은 방식으로 처리(그리디)
# -> 실패... 그리디가 최적의 해를 보장하지 않음...!
# 반례
# 5
# 1 50 60 100 1
# ans: 110
# res: 101

# import heapq

# N = int(input())

# costs = [0]

# heap = []

# costs += list(map(int, input().split()))
# for i in range(1, N+1):
#     # .append(costs[i]/i)
#     heapq.heappush(heap, (-costs[i]/i, i))  # -장당 가격, i

# answer = 0
# while N > 0:
#     cost, i = heapq.heappop(heap)
#     cost = 0 - cost

#     cnt = N//i
#     # print(cnt, cost, i)
#     # N -= cnt * i
#     N %= i
#     answer += (cnt * cost * i)

# print(int(answer))

N = int(input())

cards = [0]
dp = [0 for _ in range(N+1)]

cards += list(map(int, input().split()))
for i in range(1, N+1):
    # 1개씩 늘려가보면 되는거 -> i번에서 보자면 (dp[i-1] + cards[1]) .... (dp[1] + cards[i-1]) 중에서 제일 큰걸 선택
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + cards[j])

print(dp[N])
