import sys

N = int(sys.stdin.readline().strip())
balls = str(sys.stdin.readline().strip())
redCnt = balls.count('R')
blueCnt = balls.count('B')
answer = 0
# cnt = []

# 짧은 풀이 참고용
# # 우측으로 레드 모으기
# rexplore = balls.rstrip('R')
# cnt.append(rexplore.count('R'))

# # 우측으로 블루 모으기
# rexplore = balls.rstrip('B')
# cnt.append(rexplore.count('B'))

# # 좌측으로 레드 모으기
# lexplore = balls.lstrip('R')
# cnt.append(lexplore.count('R'))

# # 좌측으로 블루 모으기
# lexplore = balls.lstrip('B')
# cnt.append(lexplore.count('B'))

#print(min(cnt))


# case 1 R 오른쪽
cntR = 0
if balls[0] == 'R':
    for i in range(N): # 연속되는 R
        if balls[i] == 'R':
            cntR += 1
        else:
            break
    case1 = redCnt - cntR
else:
    case1 = redCnt

# case 2 R 왼쪽


