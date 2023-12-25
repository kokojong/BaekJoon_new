# 백준 22233 가희와 키워드 실2

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

keywords = set()

for _ in range(N):
    keyword = input().rstrip()
    keywords.add(keyword)

# answer = len(keywords)
# print(keywords)

for _ in range(M):
    words = list(map(str, input().rstrip().split(',')))
    # print(words)
    for word in words:
        if word in keywords:
            keywords.remove(word)
            # answer -= 1
    print(len(keywords))
    # print(answer)
