//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/19.
//

import Foundation
// 백준 11724 연결 요소의 개수

// 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다
/*
let input = readLine()!.split(separator: " ").map { Int(String($0)) ?? 0 }
let n = input.first!
let m = input.last!
var nodes: [[Int]] = Array(repeating: [], count: n+1) // key 에서 갈 수 있는 것들의 배열, 0번 인덱스 미사용
var isVisited = Array(repeating: false, count: n+1) // 0번 인덱스 미사용
var answer = 0

for _ in 0..<m {
    let line: [Int] = readLine()!.split(separator: " ").map { Int(String($0)) ?? 0 }
    let a: Int = line.first!
    let b: Int = line.last!
    nodes[a].append(b)
    nodes[b].append(a)
}

func dfs(a: Int) {
    isVisited[a] = true
    let stack = nodes[a] // a 입장에서 직접 연결된 애들
    for b in stack {
        if !isVisited[b] {
            dfs(a: b)
        }
    }
}

for i in 1...n {
    if !isVisited[i] {
        dfs(a: i)
        answer += 1
    }
}

print(answer)
*/
