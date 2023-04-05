//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/04.
//

import Foundation
// 1180 행렬 그리디 실1 

// 연산 -> 3*3 행렬의 원소를 모두 뒤집음
// 최소로 연산을 하는 횟수를 return

let input = readLine()!.components(separatedBy: " ").map { Int($0)! }

let n = input[0]
let m = input[1]

var a: [[Int]] = []
var b: [[Int]] = []

for _ in 0..<n {
    a.append(Array(readLine()!).map { Int(String($0))! } )
}

for _ in 0..<n {
    b.append(Array(readLine()!).map { Int(String($0))! } )
}

var result = 0

func isValid(r: Int, c: Int) -> Bool {
    if r + 2 > n || c + 2 > m { return false}
    return true
}

func isDiffrent(r: Int, c: Int) -> Bool {
//    for i in r...r+2 {
//        for j in c...c+2 {
            if a[r][c] != b[r][c] { return true }
//        }
//    }
    return false
}

func reverseArrayA(r: Int, c: Int) {
    for i in r...r+2 {
        for j in c...c+2 {
            a[i][j] = (a[i][j] + 1) % 2
        }
    }
    result += 1
}

func main() -> Int {
    if n < 3 || m < 3 {
        // 무조건 3 이하면 안된다고 생각해서 -1로 리턴했었음.. 어이없서..
        if a == b {
            return result
        } else {
            return -1
        }
    }
        
    for r in 0...n-3 {
        for c in 0...m-3 {
            if isValid(r: r, c: c), isDiffrent(r: r, c: c) {
                reverseArrayA(r: r, c: c)
            }
        }
        
        // 해당 행에서 다 바꿨는데 다르다면
        if a[r] != b[r] {
            return -1
        }
    }

    if a == b {
        return result
    } else {
        return -1
    }
}

print(main())

/*
 4 4
 0001
 0001
 0010
 0000
 1000
 0001
 0010
 1001
 */


