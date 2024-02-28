# 백준 19539 사과나무 골5

# 나무 1~N 높이 0
# 1 - 1만큼 성장, 2 - 2만큼 성장, 동시에 써야함. 두개 합쳐도 댐

# 주어진 배치로 만들수 있는지 여부 판단

N = int(input())

arr = list(map(int, input().split()))

if sum(arr) % 3 != 0:
    print('NO')
else:
    cnt = 0

    for i in range(N):
        cnt += (arr[i] // 2)  # 2로 나눈 몫(걸리는 일수) 만큼을 더한다..

    if cnt >= (sum(arr) / 3):
        print("YES")
    else:
        print("NO")
