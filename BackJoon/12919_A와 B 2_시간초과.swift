//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/16.
//

import Foundation

// 12919 A와 B 2 완전탐색

// 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임이다

// 문자열의 뒤에 A를 추가한다.
// 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.

/*
var answer = 0

let s = readLine()!.map { return $0 == "A" ? 0 : 1 }
let t = readLine()!.map { return $0 == "A" ? 0 : 1 }
// A -> 0, B -> 1
let n = t.count - s.count
var stack: [(s: [Int], depth: Int, op: Int)] = []


stack.append((s, 0, 1))
stack.append((s, 0, 2))

while !stack.isEmpty {
    let (s, depth, opt) = stack.removeLast()
    
    if depth == n {
        if s == t {
            answer = 1
            break
        }
        continue
    }
    
    if opt == 1 {
        var ss = s
        ss.append(0)
        stack.append((ss, depth + 1, 1))
        stack.append((ss, depth + 1, 2))
    } else {
        var ss = s
        ss.append(1)
        let reversed = ss.reversed()
        stack.append((Array(reversed), depth + 1, 1))
        stack.append((Array(reversed), depth + 1, 2))
    }
}

print(answer)


//func change1(s: [Int], depth: Int) { // 문자열 뒤에 A추가
//    if depth == n {
//        if s == t {
//            answer = 1
//            print(answer)
//            exit(0)
//        }
//        return
//    }
//    var ss = s
//    ss.append(0)
//    change1(s: ss, depth: depth + 1)
//    change2(s: ss, depth: depth + 1)
//}
//
//func change2(s: [Int], depth: Int) { // 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.
//    if depth == n {
//        if s == t {
//            answer = 1
//            print(answer)
//            exit(0)
//        }
//        return
//    }
//    var ss = s
//    ss.append(1)
//    ss.reverse()
//    change1(s: ss, depth: depth + 1)
//    change2(s: ss, depth: depth + 1)
//}
//
//change1(s: s, depth: 0)
//change2(s: s, depth: 0)

//print(s)
//if answer == 0 { print(answer) }
*/
