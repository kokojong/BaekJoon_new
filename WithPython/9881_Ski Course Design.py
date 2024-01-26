# 백준 9881 Ski Course Design 실5

# N개의 hill (1~1000)
# 0~100의 elevation
# 제일 높은거랑 낮은거의 차이가 17보다 크면 안댐

# 차이의 제곱만큼 비용이 부과

N = int(input())

arr = []

for _ in range(N):
    arr.append(int(input()))

arr.sort()

answer = []

# 17크기의 범위를 잡고 체크하기
for i in range(0, 84):
    j = i + 17
    cnt = 0
    for a in arr:
        if i <= a <= j:  # 이 범위 안에 있다면
            continue
        elif a < i:
            cnt += (i - a)**2
        elif a > j:
            cnt += (a - j)**2

    answer.append(cnt)

answer.sort()

print(answer[0])
