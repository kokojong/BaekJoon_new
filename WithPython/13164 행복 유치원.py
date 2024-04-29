# 백준 13164 행복 유치원 골5

# N명, K개 조, 1명이상, 같은 조에 있는 사람들끼리는 붙어있어야함
# 그 조에서 가장 작은, 큰 차이가 비용

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
kids = list(map(int, input().split()))

array = []
# 키차이의 배열을 만듬
for i in range(1, n):
    array.append(kids[i] - kids[i-1])

array.sort(reverse=True)  # 키차이가 큰대로 내림차순으로 정렬
print(sum(array[k-1:]))  # K-1개 만큼 뺀걸 더해줌..
