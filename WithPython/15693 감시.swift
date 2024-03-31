//
//  main.swift
//  CommandLine
//
//  Created by kokojong on 3/30/24.
//

import Foundation

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let R = input[0]
let C = input[1]

var board: [[Int]] = []
for _ in 0..<R {
    let row = readLine()!.split(separator: " ").map { Int(String($0))! }
    board.append(row)
}

//print(board)

var cctv: [[Int]] = [] // type, r, c
var total = 0 // 0이 지금 몇개인지

// 0은 빈칸, 1~5는 cctv, 6은 벽
for r in 0..<R {
    for c in 0..<C {
        if board[r][c] > 0 && board[r][c] < 6 {
            cctv.append([board[r][c], r, c])
        } else if board[r][c] == 0{
            total += 1
        }
    }
}

// 1번 오 2번 반대방향 3번 직각 4번 3방향 5번 4방향

// CC티비는 최대 8개 -> 모든 방향 다 해보기

let dr = [-1, 0, 1, 0]
let dc = [0, 1, 0, -1]

func makeFill(board: inout [[Int]], r: Int, c: Int, dir: Int) -> Int { // 감시가 추가된 영역
    var rr = r + dr[dir]
    var cc = c + dc[dir]
    
    var result = 0
    while rr >= 0 && rr < R && cc >= 0 && cc < C && board[rr][cc] < 6 {
        if board[rr][cc] == 0 {
            board[rr][cc] = -1
            result += 1
        }
        rr += dr[dir]
        cc += dc[dir]
    }
    return result
}

func watch(n: Int, r: Int, c: Int, dir: Int, board: inout [[Int]]) -> Int {
    
    var result = 0
    
    switch n {
    case 1:
        result += makeFill(board: &board, r: r, c: c, dir: dir)
        return result
    case 2:
        [0, 2].forEach {
            result += makeFill(board: &board, r: r, c: c, dir: (dir + $0) % 4)
        }
        return result
    case 3:
        [0, 1].forEach {
            result += makeFill(board: &board, r: r, c: c, dir: (dir + $0) % 4)
        }
        return result
    case 4:
        [0, 1, 2].forEach {
            result += makeFill(board: &board, r: r, c: c, dir: (dir + $0) % 4)
        }
        return result
    case 5:
        [0, 1, 2, 3].forEach {
            result += makeFill(board: &board, r: r, c: c, dir: (dir + $0) % 4)
        }
        return result
    default:
        return result
    }
}

var answer = Int.max

func DFS(i: Int, cnt: Int, board: [[Int]]) {
    if i >= cctv.count {
        let result = total - cnt
        answer = min(result, answer)
        return
    }
    
    var newBoard = board
    
    let type = cctv[i][0]
    let r = cctv[i][1]
    let c = cctv[i][2]
    
    for d in 0...3 {
        let result = watch(n: type, r: r, c: c, dir: d, board: &newBoard)
        DFS(i: i+1, cnt: cnt + result, board: newBoard)
        newBoard = board // 백트래킹
    }
}

DFS(i: 0, cnt: 0, board: board)
print(answer)
