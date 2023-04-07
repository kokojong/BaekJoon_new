//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/06.
//

import Foundation
// 21758 꿀 따기 그리디 골5
// idea: 벌 벌 통 / 벌 통 벌 / 통 벌 벌 경우로 나눠보자?

/*
let n = Int(readLine()!) ?? 0
let arr = readLine()!.split(separator: " ").map { Int(String($0))! }

// case 1 벌 벌 통
// 통은 항상 맨끝에 있는게 유리(그래야 끝까지 가니까), bee1은 무조건 맨 왼쪽에 있어야 최대가 된다.
// b1 = arr[0]
// b2 = arr[i]
// 통 = arr[n-1]
var case1 = 0
for i in 1..<n-1 { // b2의 위치
    let b1 = arr[1...n-1].reduce(0, +) - arr[i]
    let b2 = arr[i+1...n-1].reduce(0, +)
    case1 = max(case1, b1 + b2)
}
//print(case1)

// case 2 벌 통 벌
// 벌은 무조건 양 끝에 있어야 최대가 된다(꿀이 1이상이라서)
// b1 = arr[0]
// b2 = arr[n-1]
// 통 = arr[i]
var case2 = 0
for i in 1..<n-1 { // 통의 위치
    let b1 = arr[1...i].reduce(0, +)
    let b2 = arr[i...n-2].reduce(0, +)
    case2 = max(case2, b1 + b2)
}
//print(case2)


// case 3 통 벌 벌
// 통은 무조건 맨 왼쪽, b2는 맨 오른쪽
// b1 = arr[i]
// b2 = arr[n-1]
// 통 = arr[0]
var case3 = 0
for i in 1..<n-1 {
    let b1 = arr[0..<i].reduce(0, +)
    let b2 = arr[0..<n-1].reduce(0, +) - arr[i]
    case3 = max(case3, b1 + b2)
}
//print(case3)

print(max(case1, case2, case3))
*/
