//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/03.
//

import Foundation
// 11501 주식 그리디 실2

// 주식 하나를 산다.
// 원하는 만큼 가지고 있는 주식을 판다.
// 아무것도 안한다.
// 3가지 중 하나를 한다.

// idea: 올라가거나 같을 때만 산다. 내려갈때는 암것도 안한다.

/*
let t = Int(readLine()!)!

for _ in 0..<t {
    let n = Int(readLine()!)!
    let arr = readLine()!.components(separatedBy: " ").map { Int($0)! }
    
    var gain = 0 // 이득
    var cost = 0 // 지불한 가격
    var cnt = 0 // 주식 보유 수
    
    var flow: [Bool] = []
    
    for i in 0..<n - 1 {
        flow.append(arr[i] <= arr[i+1])
    }
//    print(flow)
    
    for i in 0..<n-1 {
        if flow[i] { // 앞으로 오르면 -> 주식 구매
            cnt += 1
            cost += arr[i]
        } else { // 앞으로 떨어지면 -> 주식 판매
            gain += cnt * arr[i] - cost
            cnt = 0
            cost = 0
        }
    }
    
    gain += cnt * arr[n-1] - cost
    
    print(gain)
    
}
*/
