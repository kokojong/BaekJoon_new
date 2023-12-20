# 백준 20922 겹치는건 싫어

from collections import defaultdict

N, K = map(int, input().split())

arr = list(map(int, input().split()))

dic = defaultdict(int)

left = 0
right = 0

answer = 0
while left <= right and right < N:
    if dic[arr[right]] < K:
        dic[arr[right]] += 1
        right += 1
    else:
        dic[arr[left]] -= 1
        left += 1
    answer = max(right - left, answer)
# print(left, right)
print(answer)
