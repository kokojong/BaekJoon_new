//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/23.
//

import Foundation

let n = Int(readLine()!)!
var arr: [[Int]] = []
var maxHeight = 0 // 지대의 최대 높이
for _ in 0..<n {
    let input = readLine()!.split(separator: " ").map { Int(String($0))! }
    arr.append(input)
    maxHeight = max(maxHeight, input.max()!)
}

var answer = 0
let defaultVisited = Array(repeating: Array(repeating: false, count: n), count: n)
var visited = defaultVisited

func bfsAll(h: Int) -> Int {
    var cnt = 0
    
    for i in 0..<n {
        for j in 0..<n {
            if arr[i][j] > h, !visited[i][j] {
                bfs(i: i, j: j, h: h)
                cnt += 1
            }
        }
    }

    return cnt
}

func bfs(i: Int, j: Int, h: Int) {
    let dr = [-1, 0, 1, 0]
    let dc = [0, 1, 0, -1]

    var queue: [[Int]] = []
    queue.append([i, j])

    while !queue.isEmpty {
        let q = queue.first!
        let r = q[0]
        let c = q[1]
        queue.removeFirst()

        if arr[r][c] > h { // !visited[r][c] 조건이 들어가있었다.. 생각해보니 이미 bfs로 들어갈 때 방문 처리를 해버려서 else 처리가 되었다.
            visited[r][c] = true

            for d in 0..<4 {
                let rr = r + dr[d]
                let cc = c + dc[d]

                if rr >= 0, rr < n, cc >= 0, cc < n, !visited[rr][cc], arr[rr][cc] > h {
                    visited[rr][cc] = true
                    queue.append([rr, cc])
                }
            }
        }
    }
}

// 당연히 비가 오는거라서 1부터라고 생각했는데 73퍼에서 틀리길래 설마 했는데 0도 체크를 해줘야 했다... 뭐 이딴...
for h in 0..<maxHeight {
    visited = defaultVisited
    answer = max(answer, bfsAll(h: h))
}

print(answer)
