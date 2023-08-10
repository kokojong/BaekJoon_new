//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/16.
//

import Foundation
// 1992 쿼드트리 완탐 실1

// 재귀로 해야할듯 -> 처음에 전체 크기에 대해서 같은지 판단 -> 안되면 ()를 붙이고 다시 1/4씩 나눈다. 반복?

/*
var n = Int(readLine()!) ?? 0
var board: [[Int]] = []
var answer = ""
for _ in 0..<n {
    board.append(Array(readLine()!.map{ Int(String($0))! }))
}

func checkQuad(r: Int, c: Int, k: Int) -> Bool {
    let value = board[r][c] // 처음 값
    
    for i in r..<r+k {
        for j in c..<c+k {
            if board[i][j] != value {
                return false
            }
        }
    }
    return true
}

func quad(r: Int, c: Int, k: Int) { // [r][c] 에서 시작해서 크기가 k
    let value = board[r][c] // 처음 값
    if k == 1 {
        answer += "\(value)"
        return
    }
    
    if checkQuad(r: r, c: c, k: k) {
        answer += "\(value)"
    } else {
        answer += "("
        quad(r: r, c: c, k: k/2)
        quad(r: r, c: c + k/2, k: k/2)
        quad(r: r + k/2, c: c, k: k/2)
        quad(r: r + k/2, c: c + k/2, k: k/2)
        answer += ")"
    }
}

quad(r: 0, c: 0, k: n)
print(answer)
*/
