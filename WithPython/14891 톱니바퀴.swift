// K번 회전 시키기
// 맞닿은 극에 따라서 회전 가능
// 돌렸을 때 극이 다르면 B는 A의 반대방향으로 회전

// N극은 0, S극은 1

//
//  main.swift
//  CommandLine
//
//  Created by kokojong on 3/30/24.
//

// K번 회전 시키기
// 맞닿은 극에 따라서 회전 가능
// 돌렸을 때 극이 다르면 B는 A의 반대방향으로 회전

// N극은 0, S극은 1

import Foundation

var arr: [[Int]] = []

for i in 0..<4 {
    let info = readLine()!.map{ Int(String($0))! }
//    print(info)
    arr.append(info)
}

//print(arr)

let K = Int(readLine()!)!

func turn(n: Int, r: Int) {
    var now = arr[n]
    if r == 1 { // 시계방향
        now = [now.removeLast()] + now
    } else {
        now.append(now.removeFirst())
    }
//    print("now", now)
    arr[n] = now // 적용해주기
}

func check(n: Int, r: Int, state: [Bool]) { // 이미 움직인건지 체크용
    var tmpState = state
    tmpState[n] = true
    
    if n > 0 { // 왼쪽 체크
        let left = n - 1
        if arr[left][2] != arr[n][6] && !state[left] { // 또 돌아
            check(n: left, r: -r, state: tmpState)
        }
    }
    
    if n < 3 { // 오른쪽 체크
        let right = n+1
        if arr[n][2] != arr[right][6] && !state[right] {
            check(n: right, r: -r, state: tmpState)
        }
    }
    
    turn(n: n, r: r)
}

//turn(n: 0, r: 1)
//turn(n: 0, r: -1)

for _ in 0..<K {
    let input = readLine()!.split(separator: " ").map{ Int($0)! }
    let num = input[0] - 1
    let round = input[1]
    check(n: num, r: round, state: Array(repeating: false, count: 4)) // 실제로 얘 먼저 돌려줌
}

var answer = 0

for i in 0...3 {
    if arr[i][0] == 1 {
        answer += Int(pow(2.0, Double(i)))
    }
}

print(answer)
