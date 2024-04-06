import Foundation

// 백준 10830 행렬 제곱 골4

let NB = readLine()!.split(separator: " ").map { Int(String($0))! }
let N = NB[0]
var B = NB[1]

var board: [[Int]] = []

for _ in 0..<N {
    let row = readLine()!.split(separator: " ").map { Int(String($0))! % 1000 } // 미리 1000 나머지 처리
    board.append(row)
}

func multi(_ matrix1: [[Int]], _ matrix2: [[Int]]) -> [[Int]] {
    var result: [[Int]] = Array(repeating: Array(repeating: 0, count: N), count: N)
    
    for i in 0..<N {
        for j in 0..<N {
            for k in 0..<N {
                result[i][j] += matrix1[i][k] * matrix2[k][j] // 행렬의 곱셈
                result[i][j] %= 1000
            }
        }
    }
    return result
}

var odd: [[Int]] = []

while B > 1 {
    if B % 2 == 1 {
        if odd.isEmpty {
            odd = board
        } else {
            odd = multi(board, odd)
        }
    }
    
    // 제곱하기
    board = multi(board, board)
    
    B /= 2
}

if !odd.isEmpty {
    board = multi(board, odd)
}

for r in 0..<N {
    let row = board[r].map { String($0) }.joined(separator: " ")
    print(row)
}



