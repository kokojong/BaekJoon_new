import Foundation

// 백준 11559 puyo puyo 골4

// 4개 이상 연결 되어있으면 한번에 없어짐, 연쇄 1시작
// 중력 적용
// 터질수 있는게 여러개면 동시에

var board: [[String]] = []

for _ in 0..<12 {
    let input = Array(readLine()!.map { String($0) })
    board.append(input)
}

let dr = [-1, 0, 1, 0]
let dc = [0, -1, 0, 1]

var answer = 0

while true {
    if check() { // 이미 터진 상태면
        answer += 1
        gravity(board: &board)
    } else {
        break
    }
}

print(answer)

func check() -> Bool {
    var visited = Array(repeating: Array(repeating: false, count: 6), count: 12)
    var isCombo = false
    for r in 0..<12 {
        for c in 0..<6 {
            if board[r][c] != "." {
                let result = BFS(r, c, board: &board, visited: &visited)
                if result.count >= 4 {
                    for rc in result {
                        let rr = rc[0]
                        let cc = rc[1]
                        board[rr][cc] = "." // 터트림
                        isCombo = true
                    }
                }
            }
        }
    }
    
    return isCombo
}

func BFS(_ r: Int, _ c: Int, board: inout [[String]], visited: inout [[Bool]]) -> [[Int]] { // r, c에서 터질수 있는게 있는지 체크해 줌
    // path: 내 경로 저장용
    visited[r][c] = true
    
    var queue: [[Int]] = [[r, c]]
    var idx = 0
    
    let k = board[r][c]
    
    while idx < queue.count {
        let q = queue[idx]
        let qr = q[0]
        let qc = q[1]
        
        for i in 0..<4 {
            let rr = qr + dr[i]
            let cc = qc + dc[i]
            
            if rr >= 0 && rr < 12 && cc >= 0 && cc < 6 && board[rr][cc] == k && visited[rr][cc] == false {
                visited[rr][cc] = true
                queue.append([rr, cc])
            }
        }
        
        idx += 1
    }
    
    return queue
}

func gravity(board: inout [[String]]) {
    var columns: [[String]] = []
    for C in 0..<6 {
        var column: [String] = [] // 얘를 큐처럼..?
        for R in 0..<12 {
            column.append(board[R][C])
        }
        
        var newColumn: [String] = []
        for i in 0..<12 {
            if column[i] != "." {
                newColumn.append(column[i])
            }
        }
        
        newColumn = Array(repeating: ".", count: 12 - newColumn.count) + newColumn
        columns.append(newColumn)
    }
    
    for r in 0..<12 {
        for c in 0..<6 {
            board[r][c] = columns[c][r]
        }
    }
//    print("new board", board)
}
