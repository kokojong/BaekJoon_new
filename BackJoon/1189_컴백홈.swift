//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/12.
//

import Foundation

// 1189 컴백홈 완탐 실1
// idea: k번만큼 이동했을 때 딱 집에 도착한 경우를 구한다.

// TIL: dfs로 하면 스텍오버플로우가 발생할 수 있음(특히 board를 계속 다시 호출하게 되어서)
// board에 방문처리를 다시 롤백해주고 dfs를 돌리는 방법으로 하자!
// inout과 &를 활용해서 주소에 접근 가능

/*
let input = readLine()!.components(separatedBy: " ")
let R = Int(input[0])!
let C = Int(input[1])!
let K = Int(input[2])!

// [r-1][0] 에서 시작, [0][c-1] 까지 이동
var board: [[Character]] = []
for _ in 0..<R {
    board.append(Array(readLine()!))
}

var answer = 0

func dfs(board: inout [[Character]], r: Int, c: Int, depth: Int) {
    var board = board
    let dr = [-1, 0, 1, 0]
    let dc = [0, 1, 0, -1]
    
    if depth > K {
        return
    }
    
    if depth == K, r == 0, c == C-1 {
        answer += 1
    } else {
        for i in 0..<4 {
            let rr = r + dr[i]
            let cc = c + dc[i]
            if rr >= 0, rr < R, cc >= 0, cc < C {
                if board[rr][cc] == "." { // 미방문시
                    board[rr][cc] = "X"
                    dfs(board: &board, r: rr, c: cc, depth: depth + 1)
                    board[rr][cc] = "."
                    
                }
            }
        }
    }
    
}

if board[R-1][0] == "." {
    board[R-1][0] = "X"
    dfs(board: &board, r: R-1, c: 0, depth: 1)
} else {
    answer = 0
}

print(answer)
*/
