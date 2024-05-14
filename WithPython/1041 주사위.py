# 백준 1041 주사위 골5

N = int(input())
dices = list(map(int, input().split()))

nums = []
nums.append(min(dices[0], dices[5]))
nums.append(min(dices[1], dices[4]))
nums.append(min(dices[2], dices[3]))
nums.sort()

case1 = min(dices)  # 가장 작은 값
case2 = nums[0] + nums[1]
case3 = nums[0] + nums[1] + nums[2]

answer = 0
if N == 1:
    answer = sum(dices) - max(dices)  # 가장 큰거 빼고
else:
    answer += 4*case3  # 꼭지점
    answer += 4*case2*(N-1 + N-2)  # 모서리(위4 + 옆4)

    answer += 5*case1*(N-2)*(N-2)  # 5방향의 가운데 파낸거
    answer += 4*case1*(N-2)  # 바닥에 붙은 모서리 4개

print(answer)
