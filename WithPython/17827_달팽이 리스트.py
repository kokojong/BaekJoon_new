# 백준 17827 달팽이 리스트 실2
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())  # 노드 갯수, 질문 갯수, 연결된 노드 번호(사이클 형성하는)
arr = list(map(int, input().split()))

cycle = N - V + 1  # 사이클의 크기
left = N - cycle
# print("cycle", cycle, left)
for _ in range(M):
    i = int(input())

    if i <= left:
        # print("답1", i, arr[i])
        print(arr[i])
    else:
        i -= left
        m, n = i//cycle, i % cycle  # 몫, 나머지
        print(arr[left + n])
        # i += left
        # print("답2", i, n, arr[left + n])
