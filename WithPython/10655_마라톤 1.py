# 백준 10655 마라톤1 실3

# 1~N의 체크포인트를 모든거 순서대로 방문후 N에서 끝나야함
# 1,N만 아닌 것중에 1개 건너뛰기

N = int(input())

arr = []

for i in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

# 매번 다 계산을 하게 되면 10만 * 10만이라서 안될듯?

accum = []

for i in range(N-1):
    x1, y1 = arr[i]
    x2, y2 = arr[i+1]
    cost = abs(x1-x2) + abs(y1-y2)
    accum.append(cost)

# accum의 i번쨰는 i->i+1로 갈때의 거리

acc = sum(accum)
answer = acc

for i in range(N-2):
    # i -> i+1로 가는걸 건너뛰어보기 i -> i+2로 이동
    new = acc - accum[i] - accum[i+1]
    x1, y1 = arr[i]
    x2, y2 = arr[i+2]
    cost = abs(x1-x2) + abs(y1-y2)
    new += cost
    answer = min(answer, new)

print(answer)
