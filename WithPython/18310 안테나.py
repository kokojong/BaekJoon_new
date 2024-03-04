# 백준 18310 안테나 실3

# 집이 위치한 곳만 가능, 동일한 위치에 여러집 가능

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

# 하나하나 해보면 10만 * 20만 -> 200억

# idea 애들을 줄세워서 중간에 있는거로 하면 안되나??
# 집위에만 설치할 수 있는거라서!
answer = arr[(N-1) // 2]
print(answer)
