//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/22.
//

import Foundation
// 백준 2644 촌수계산 bfs 실버2

let n = Int(readLine()!) ?? 0 // 총 인원수
let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let a = input[0] // 구해야 하는 두 사람의 번호
let b = input[1]

let m = Int(readLine()!) ?? 0 // 관계 수
var relation: [[Int]] = Array(repeating: Array<Int>(), count: n+1) // (x, y) x가 y의 부모
// index가 부모, value가 자식의 배열 -> arr[1] = [2,3] -> 1라는 부모가 2,3의 자식을 갖기
for _ in 0..<m {
    let line = Array(readLine()!.split(separator: " ").map { Int(String($0))! })
    relation[line[0]].append(line[1])
}

var visited: [Bool] = Array(repeating: false, count: n+1)

var answer = -1

// idea: 내가 부모인 경우, 내가 자식인 경우 모두 지나가면서 depth를 1씩 올려줌. target에 도착하면 멈추기 또는 부모나 자식이 더이상 엎으면 return
func bfs(a: Int, target: Int, depth: Int) {
    
    visited[a] = true
    
    if a == target {
        answer = depth
        return
    }
    
    // 부모 탐색
    var parent = 0
    for i in 1...n {
        if relation[i].contains(a) { // 나를 자식으로 가지고 있다면
            parent = i
        }
    }
    if parent != 0, !visited[parent] { // 나를 자식으로 가진 부모가 있고 방문 전이라면
        bfs(a: parent, target: b, depth: depth + 1)
    }
    
    // 자식 탐색
    let child = relation[a]
    if !child.isEmpty {
        for c in child {
            if !visited[c] {
                bfs(a: c, target: b, depth: depth + 1)
            }
        }
    }
    
}

bfs(a: a, target: b, depth: 0)
print(answer)
