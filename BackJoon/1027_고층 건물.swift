//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/18.
//

import Foundation

// 백준 1027 고층 건물 완탐 골4
/*
let n = Int(readLine()!) ?? 0
let arr: [Double] = readLine()!.split(separator: " ").map { Double(String($0))! }
var answer = 0

func findLeft(x1: Int) -> Int { // 기준점의 왼쪽에 몇개가 되는지
    var leftCnt = 0
    let y1 = arr[x1]
    var maxD: Double = Double(Int.max)
    
    for l in 1...x1 {
        let x2 = x1 - l
        let y2 = arr[x2]
        let d = Double(y2 - y1) / Double(x2 - x1)
        if d < maxD { // 기울기는 양수, 그 중 최근에 나온 가장 큰 기울기보다 작은 기울기가 나와야만 가능
            leftCnt += 1
            maxD = d
        }
    }
    
    return leftCnt
    
}

func findRight(x1: Int) -> Int { // 기준점의 오른쪽에 몇개가 되는지
    var rightCnt = 0
    let y1 = arr[x1]
    var minD: Double = Double(Int.min)
    
    for l in x1+1..<n {
        let x2 = l
        let y2 = arr[x2]
        let d = Double(y2 - y1) / Double(x2 - x1)
        if d > minD { // 기울기는 음수, 그 중 최근에 나온 가장 작은 기울기보다 큰 기울기가 나와야만 가능
            rightCnt += 1
            minD = d
        }
    }
    return rightCnt
}
    
for i in 0..<n {
    var left = 0
    var right = 0
    if i > 0 {
        left = findLeft(x1: i)
    }
    
    if i < n-1 {
        right = findRight(x1: i)
    }
    
//    print(left, right)
    answer = max(left + right, answer)
}

print(answer)
*/
