import Foundation

// 백준 6987 월드컵 골4

// 6개의 팀이 각각 한번씩 총 5번 경기를 치름.

var posibles: [[Int]] = []

for i in 0..<6 {
    for j in i+1..<6 {
        posibles.append([i, j]) // i랑 j랑 경기함
    }
}

var answers: [Int] = []
var isPosible: Bool = true

var board: [[Int]] = []

for _ in 0..<4 {
    let input = readLine()!.split(separator: " ").map { Int(String($0))! }
    board = [] // board[i] 번째에 승, 무, 패를 기록함
    for i in 0..<6 {
        let w = input[i*3]
        let d = input[i*3+1]
        let l = input[i*3+2]
        board.append([w, d, l])
    }
    isPosible = false
    DFS(depth: 0, board: &board)
    answers.append(isPosible ? 1 : 0)
}

print(answers.map{ String($0) }.joined(separator: " "))

func DFS(depth: Int, board: inout [[Int]]) {
//    print("depth", depth, board)
    if depth == 15 {
        var win = 0
        var draw = 0
        var lose = 0
        
        for i in 0..<6 {
            win += board[i][0]
            draw += board[i][1]
            lose += board[i][2]
        }
//        print(win, draw, lose)
        if win + draw + lose == 0 {
            isPosible = true
        }
        return
    }
    
    let A = posibles[depth][0]
    let B = posibles[depth][1]
    
    // A랑 B를 선택 한 다음에 해당 경기들의 결과를 대입해봄, DFS하고 다시 백트래킹
    // A가 이김,
    for (a, b) in [(0, 2), (1, 1), (2, 0)] { // 승,패 무,무 패,무
        if board[A][a] > 0 && board[B][b] > 0 {
            board[A][a] -= 1
            board[B][b] -= 1
            DFS(depth: depth+1, board: &board)
            board[A][a] += 1
            board[B][b] += 1
        }
    }
}
