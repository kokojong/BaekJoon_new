# 백준 20920 영단어 암기는 괴로워 실3

# 자주 나오는 단어일수록 앞에 배치
# 해당 단어의 길이가 길수록 앞에 배치
# 사전순으로 앞에 배치

# 길이가 M이상인 단어만 만듬!

from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dict = defaultdict(int)

answers = []

for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if dict[word] == 0:
            answers.append(word)
        dict[word] += 1

answers.sort(key=lambda x: (-dict[x], -len(x), x))

# print("answers", answers)
for answer in answers:
    print(answer)
