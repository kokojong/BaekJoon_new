# 백준 20291 파일 정리 실3

# 확장자 별로 몇개 있는지
# 확장자들을 사전순으로 정렬

from collections import defaultdict

N = int(input())

ex = set()  # 확장자명
dic = defaultdict(int)

for _ in range(N):
    name, exten = map(str, input().split('.'))
    # print(name, exten)

    ex.add(exten)

    dic[exten] += 1

ex = list(ex)
ex.sort()

for e in ex:
    print(e, dic[e])
