//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/26.
//

import Foundation
// 백준 2512 예산 이분탐색 실3

/*
let n = Int(readLine()!)!
let arr: [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
let m = Int(readLine()!)!

var answer = 0

// idea: 제일 큰 수에서 부터 이분탐색으로 찾기

func binarySearch(l: Int, r: Int) {
    let mid = (l + r) / 2
    if mid == l || mid == r { // left가 Mid랑 같아짐 -> 탐색 종료
        return
    }
    var total = 0
    for a in arr {
        if a > mid { total += mid }
        else { total += a }
    }
//    print("total", total, "l, mid, r", l, mid, r)
    
    if total > m { // 상한이 너무 높음
        binarySearch(l: l, r: mid)
    } else {
        answer = max(answer, mid)
        binarySearch(l: mid, r: r)
    }
}

if arr.reduce(0, +) <= m {
    answer = arr.max()!
} else {
    binarySearch(l: 0, r: arr.max()!)
}

print(answer)
*/
