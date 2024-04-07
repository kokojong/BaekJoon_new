import Foundation

// 백준 2559 수열 실3

// 연속적인 며칠동안의 온도의 합이 가장 큰 값 찾기

let NK = readLine()!.split(separator: " ").map { Int(String($0))! }
let N = NK[0]
let K = NK[1]

let arr: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }

var accum: [Int] = [0] // 누적 합

for i in 0..<N {
    accum.append(accum.last! + arr[i])
}
//print(accum)

var answer = Int.min

for i in 1...(N-K+1) {
    let j = i + K - 1
    let tmp = accum[j] - accum[i-1]

    answer = max(tmp, answer)
}

print(answer)