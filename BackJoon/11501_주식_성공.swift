//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/04.
//

import Foundation
// 11501 주식 그리디 실2

// idea (컨닝): 뒤에서부터 탐색을 해서 최대값을 갱신해주면서 구매 판매 판단

/*
let t = Int(readLine()!)!

for _ in 0..<t {
    let n = Int(readLine()!)!
    let arr = Array(readLine()!.split(separator: " ").map { Int(String($0))! }.reversed())
    
    var gain = 0
    var maxPrice = arr.first!
    
    for value in arr {
        if value >= maxPrice {
            maxPrice = value
        } else {
            gain += (maxPrice - value)
        }
    }
    
    print(gain)
    
}
*/

let t = Int(readLine()!)!

for _ in 0..<t {
    let n = Int(readLine()!)!
    let arr = Array(readLine()!.split(separator: " ").map { Int(String($0))! }.reversed())
    
    var gain = 0
    var maxValue = arr[0] // 원래 제일 끝 값 -> 현재는 처음 값
    
    for value in arr {
        if value >= maxValue {
            maxValue = value // 갱신
            gain += 0
        } else {
            gain += (maxValue - value)
        }
    }
    print(gain)
}
