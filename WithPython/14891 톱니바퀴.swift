// K번 회전 시키기
// 맞닿은 극에 따라서 회전 가능
// 돌렸을 때 극이 다르면 B는 A의 반대방향으로 회전

// N극은 0, S극은 1

import Foundation

var arr: [[Int]] = []

for i in 0..<4 {
    let info = readLine()!.map{ Int($0) }
    print(info)
}

let K = Int(readLine()!)!

for _ in 0..<K {
    let input = readLine()!.split(' ').map{ Int($0)! }
    print(input)
}