# 백준 1062 가르침 골4

import sys
from itertools import combinations
input = sys.stdin.readline

N, K = map(int, input().split())

# N: 단어의 갯수 K: 가르칠 수 있는 글자 - 이 글자로만 이루어진 단어만을 읽을 수 있음

# 기본적으로 anta 와 tica가 들어있어야함

visited = {'a', 'n', 't', 'i', 'c'}
toVisit = set()
arr = []

for _ in range(N):
    word = input()
    arr.append(word[4:-5])
    for w in word[4:-5]:
        if w not in visited:
            toVisit.add(w)
# print(arr)
# print(toVisit)
if K < 5:
    print(0)
elif K == 26 or K-5 >= len(toVisit):
    print(N)
else:
    answer = 0

    for comb in combinations(toVisit, K-5):  # K-5개를 직접 고름 -> 모든 애들 다 포함 가능한지 체크
        cnt = 0
        # print("comb", comb)

        for word in arr:
            flag = True  # comb와 visited만으로 처리가 가능한지
            for w in word:
                if w in visited or w in comb:
                    continue
                else:
                    flag = False
                    break
            cnt += flag
        answer = max(answer, cnt)

    print(answer)
