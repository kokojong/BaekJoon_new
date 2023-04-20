//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/20.
//

import Foundation
// 백준 1743 음식물 피하기

let input = readLine()!.split(separator: " ").map { Int(String($0)) ?? 0 }
let n = input[0]
let m = input[1] // n행 m열
let k = input[2]

var board: [[Int]] = Array(repeating: Array(repeating: 0, count: m), count: n) // 빈곳은 0, 쓰레기가 있는곳은 -1로 하자!

for _ in 0..<k {
    let line = readLine()!.split(separator: " ").map { Int(String($0)) ?? 0 }
    board[line[0] - 1][line[1] - 1] = -1
}

var cnt = 0
var answer = 0 // 가장 큰 쓰레기의 크기

func dfs(r: Int, c: Int) { // cnt: 연속된 쓰레기의 크기
    if board[r][c] == -1 {
        let dr = [-1, 0, 1, 0]
        let dc = [0, 1, 0, -1]
        
        for d in 0..<4 {
            let rr = r + dr[d]
            let cc = c + dc[d]
            
            if rr >= 0, rr <= n-1, cc >= 0, cc <= m-1 {
                board[r][c] = 0
                dfs(r: rr, c: cc)
            }
        }
        cnt += 1
//        return
    }
//    return
    
}

for r in 0..<n {
    for c in 0..<m {
        cnt = 0 // 초기화
        if board[r][c] == -1 { 
            dfs(r: r, c: c)
            answer = max(answer, cnt)
        }
    }
}

print(answer)
