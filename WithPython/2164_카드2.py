# 백준 2164 카드2 실4

from collections import deque
N = int(input())

cards = deque([])
for i in range(1, N+1):
    cards.append(i)
# print(cards)

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])
