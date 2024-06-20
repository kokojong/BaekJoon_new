# 백준 4358 생태학 실2

from collections import defaultdict
import sys
input = sys.stdin.readline

dic = defaultdict(int)

total = 0
while True:
    word = input().rstrip()
    if word == '':
        break
    dic[word] += 1
    total += 1

for (k, v) in sorted(dic.items()):
    percent = v/total * 100
    print("%s %.4f" % (k, percent))
