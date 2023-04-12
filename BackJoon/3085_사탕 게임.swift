//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/07.
//

import Foundation
// 3085 사탕 게임 완탐 실2

// 아.......... 헛짓거리 해따..

/*
let n = Int(readLine()!) ?? 0
var board: [[Character]] = []
for _ in 0..<n {
    board.append(Array(readLine()!))
}

var answer = 0
//print(board)

func changeBoard(r: Int, c: Int){
    var changedBoard = board
    let dx = [-1, 0, 1, 0] // column
    let dy = [0, 1, 0, -1] // row
    for i in 0..<4 {
        let rr = r + dy[i]
        let cc = c + dx[i]
        if rr >= 0 && rr < n && cc >= 0 && cc < n {
            changedBoard[rr][cc] = board[r][c]
            changedBoard[r][c] = board[rr][cc]
            search(changedBoard)
        }
    }
}

func search(_ board: [[Character]]) -> Int {
    var maxCnt = 0
    let dc = [-1, 0, 1, 0] // column
    let dr = [0, 1, 0, -1] // row
    var visited = Array(repeating: Array(repeating: 0, count: n), count: n) // 미방문시 0으로 처리하기, 방문시 해당 숫자만큼 늘리기
    var stack: [(Int, Int)] = []
    
    for i in 0..<n {
        for j in 0..<n {
            if visited[i][j] == 0 {
                let now = board[i][j]
                visited[i][j] += 1 // 방문처리
                for k in 0..<4 {
                    let rr = i + dr[k]
                    let cc = j + dc[k]
                    if rr >= 0, rr < n, cc >= 0, cc < n, now == board[rr][cc] { // in range, same
                        stack.append((rr,cc))
//                        visited[rr][cc] = visited[i][j] + 1
                    }
                }
            }
        }
    }
    
    print("visited", visited)
    
    visited.forEach {
        maxCnt = max(maxCnt, $0.max()! )
    }
    return maxCnt
}

for i in 0..<n {
    for j in 0..<n {
        changeBoard(r: i, c: j)
    }
}
*/

// 아... 헛짓거리 함...
// 문제는 '가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다' 였는데
// dfs를 하다가 막혔다 ㅋㅋㅋㅋㅋㅋㅋㅋ 다시 작성 시작...!

/*
let n = Int(readLine()!) ?? 0
var board: [[Character]] = []
for _ in 0..<n {
    board.append(Array(readLine()!))
}

var answer = 0

func changeBoard(_ board: [[Character]], r: Int, c: Int) {
    let dx = [-1, 0, 1, 0] // column
    let dy = [0, 1, 0, -1] // row
    for i in 0..<4 {
        let rr = r + dy[i]
        let cc = c + dx[i]
        if rr >= 0 && rr < n && cc >= 0 && cc < n {
            var changedBoard = board // 놓친 부분 -> 4방향으로 갈때마다 보드를 초기화 해야하는데 그전에 초기화해서 정보가 남아버림..
            changedBoard[rr][cc] = board[r][c]
            changedBoard[r][c] = board[rr][cc]
            answer = max(answer, cntRowMax(changedBoard), cntColumnMax(changedBoard))
        }
    }
}

func cntRowMax(_ board: [[Character]]) -> Int {
    var maxCnt = 0
    for i in 0..<n {
        var rowCnt = 1
        for j in 0..<n-1 {
            if board[i][j] == board[i][j+1] {
                rowCnt += 1
            } else  {
                maxCnt = max(maxCnt, rowCnt)
                rowCnt = 1
            }
        }
        maxCnt = max(maxCnt, rowCnt) // 놓쳤던 부분 - 계속 같은거면 maxCnt가 갱신이 안댐
    }
    return maxCnt
}

func cntColumnMax(_ board: [[Character]]) -> Int {
    var maxCnt = 0
    for i in 0..<n {
        var columnCnt = 1
        for j in 0..<n-1 {
            if board[j][i] == board[j+1][i] {
                columnCnt += 1
            } else {
                maxCnt = max(maxCnt, columnCnt)
                columnCnt = 1
            }
        }
        maxCnt = max(maxCnt, columnCnt) // 놓쳤던 부분 - 계속 같은거면 maxCnt가 갱신이 안댐
    }
    return maxCnt
}

for i in 0..<n {
    for j in 0..<n {
        changeBoard(board, r: i, c: j)
    }
}

print(answer)
*/
