# 백준 2564 경비원 실1

w, h = map(int, input().split())
n = int(input())
# 1 - 북, 2 - 남, 3 - 서, 4 - 동
# 둘쨰숫자는 왼쪽으로부터의 거리(x좌표)

arr = [list(map(int, input().split())) for _ in range(n)]
now = list(map(int, input().split()))
# print(arr)
# print(now)


def cal_distance(x, y):
    if x == 1:
        return y
    elif x == 2:
        return w + (w-y) + h
    elif x == 3:
        return w + h + w + (h-y)
    elif x == 4:
        return w + y


answer = 0
dis = []
for a in arr:
    dis.append(cal_distance(a[0], a[1]))
now = cal_distance(now[0], now[1])

for d in dis:
    clockWise = abs(now - d)
    counterClockWise = 2*w + 2*h - clockWise
    answer += min(clockWise, counterClockWise)

print(answer)
