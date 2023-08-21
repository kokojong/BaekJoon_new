# 백준 15686 치킨 배달 골5

# M개의 치킨집만 남기고 다 없앤다음에 도시의 치킨 거리의 총합이 작게 될지 고르기!!
# 치킨 거리 총합의 최솟값 print

from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []
chickens = []  # 치킨집의 좌표 모음
houses = []
# 0은 빈 칸, 1은 집, 2는 치킨집이다.
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

for r in range(N):
    for c in range(N):
        if board[r][c] == 2:
            chickens.append((r, c))
        elif board[r][c] == 1:
            houses.append((r, c))

posibles = list(combinations(chickens, M))  # M개 고른 컴비네이션 -> 살아남은 치킨집

answer = 10000
for posible in posibles:
    tmp = 0
    for hr, hc in houses:  # 집과 치킨집을 하나씩 매칭해보고 최단 거리 찾기
        chick_dis = 10000
        for cr, cc in posible:  # 틀린 부분: 여기서 chickens로 해서 폐업한 애들을 모조리 세어버려따...
            chick_dis = min(chick_dis, abs(hr - cr) + abs(hc - cc))
        tmp += chick_dis

    answer = min(answer, tmp)

print(answer)
