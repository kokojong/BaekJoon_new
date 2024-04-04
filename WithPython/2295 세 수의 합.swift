// 백준 2295 세 수의 합 골5 이분탐색

// 적당히 세수를 골랐을 때 그 합 d도 집합에 포함되는 경우 중 가장 큰 d

let N = Int(readLine()!)! // 1000 이하
var arr: [Int] = []
for _ in 0..<N {
    arr.append(Int(readLine()!)!)
}

arr.sort()

// x, y, z, k
// x, y 를 골라서 x+y = k-z 가 되도록?

var sums: Set<Int> = []
for x in arr {
    for y in arr {
        sums.insert(x+y)
    }
}

var answer: [Int] = []
for k in arr {
    for z in arr {
        let result = k - z
        if sums.contains(result) {
            answer.append(k)
        }
    }
}

answer.sort()
print(answer.last!)