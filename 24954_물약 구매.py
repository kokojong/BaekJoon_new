# 백준 24954 물약 구매 실1
# 쇼미더코드 1번 문제

from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())

costs = [0]
for k in list(map(int, input().split())):  # index 맞춰주기
    costs.append(k)
discounts = [[] for _ in range(N)]

for i in range(N):
    p = int(input())  # p개의 할인 정보가 주어진다 -> i번째 물약을 사면~
    for j in range(p):
        a, d = map(int, input().split())  # a물약을 d만큼 할인
        # i번 물약을 구매하고 나면 aj가 dj만큼 할인된다는 뜻
        discounts[i].append((a, d))

# print(costs)
# print(discounts)

posibles = list(permutations(range(1, N+1), N))
# print(posibles)

# answer = -1
answers = []
for posible in posibles:
    posible = list(posible)
    newCost = costs[:]
    result = 0
    # print(posible)
    for p in posible:  # 뭐부터 물약정보를 업데이트 할 지 선택 -> p는 선택한 물약의 번호
        result += newCost[p]
        for dis in discounts[p-1]:
            a, d = dis
            newCost[a] = max(1, newCost[a] - d)  # 1이상이어야함
            # newCost[a] = newCost[a] - d
            # if newCost[a] < 1:
            #     newCost[a] = 1

    answers.append(result)
    # if answer < 0 or result < answer:
    #     answer = result
# print(answers)
print(min(answers))
# print(answer)
