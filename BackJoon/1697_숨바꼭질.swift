//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/23.
//

import Foundation
// 백준 1697 숨바꼭질 BFS 실1

let input = readLine()!.split(separator: " ").map { Int(String($0)) ?? 0 }
let n = input[0]
let k = input[1]
let max = Int(1e5) + 1

var visit: [Bool] = Array(repeating: false, count: max) // 넉넉히 10만으로 처리? -> k보다 큰 점에서 뒤로 올수도 있음
var queue: [Int] = []
var depth: [Int] = Array(repeating: 0, count: max)
var answer = -1

queue.append(n)
visit[n] = true
while !queue.isEmpty {
    let q = queue.removeFirst()
    if q == k {
        answer = depth[k]
        break
    }
    
    if q+1 < max, !visit[q+1] {
        queue.append(q+1)
        depth[q+1] = depth[q] + 1
        visit[q+1] = true
    }
    
    if q-1 >= 0, !visit[q-1] {
        queue.append(q-1)
        depth[q-1] = depth[q] + 1
        visit[q-1] = true
    }
    
    if q*2 < max, !visit[q*2] {
        queue.append(q*2)
        depth[q*2] = depth[q] + 1
        visit[q*2] = true
    }
}

print(answer)
