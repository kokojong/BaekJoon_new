# 백준 9470 starhler 순서 골3

from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline


T = int(input())
# 나머지 노드는 그 노드로 들어오는 강의 순서 중 가장 큰 값을 i라고 했을 때,
# 들어오는 모든 강 중에서 Strahler 순서가 i인 강이 1개이면 순서는 i, 2개 이상이면 순서는 i+1이다.
# -> 들어오늠 모든 강에서의 순서를 알아서 세야함
for _ in range(T):
    K, N, V = map(int, input().split())  # TC 번호, 노드수(마지막은 바다), 간선수

    degrees = [0 for _ in range(N+1)]
    graphs = [[] for _ in range(N+1)]

    starDic = [defaultdict(int) for _ in range(N+1)]
    starList = [-1 for _ in range(N+1)]  # 결과값

    for _ in range(V):
        a, b = map(int, input().split())  # a -> b
        graphs[a].append(b)  # a 다음에 갈것 b
        degrees[b] += 1

    queue = deque()

    for i in range(1, N+1):
        if degrees[i] == 0:
            queue.append(i)
            starList[i] = 1  # star 값 1로

    while queue:
        q = queue.popleft()
        current = starList[q]

        for g in graphs[q]:
            degrees[g] -= 1
            starDic[g][current] += 1  # g번째 딕셔너리의 current 값을 1 올림

            if degrees[g] == 0:
                queue.append(g)
                next = max(starDic[g].keys())  # 딕셔너리에서 가장 큰 값을 가져와서 넣음

                if starDic[g][next] > 1:
                    starList[g] = next + 1
                else:
                    starList[g] = next

    # print(starList)
    print(K, starList[N])
