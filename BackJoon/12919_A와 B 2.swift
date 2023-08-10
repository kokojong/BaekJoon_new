//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/17.
//

import Foundation

// 12919 A와 B 2 완전탐색

// 두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임이다

// 문자열의 뒤에 A를 추가한다. - case1
// 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다. - case2

// 틀렸던 이유: s -> t가 아니라 t -> s로 해야한다.

/*
let s = readLine()!.map { return $0 == "A" ? 0 : 1 }
let t = readLine()!.map { return $0 == "A" ? 0 : 1 }
// A -> 0, B -> 1
let n = t.count - s.count

// 반대로 하니까
// 끝이 A라면 -> case1(A를 빼줌)
// 맨 앞이 B라면 -> case2(뒤집고 맨뒤에 B를 빼줌)

func dfs(arr: [Int]) {
    if arr.count == s.count {
        if arr == s {
            print(1)
            exit(0)
        }
        return
    }
    
    let last = arr.last!
    if last == 0 {
        var tmp = arr
        tmp.removeLast()
        dfs(arr: tmp)
    }
    
    let first = arr.first!
    if first == 1 {
        var tmp = Array(arr.reversed())
        tmp.removeLast()
        dfs(arr: tmp)
    }
    
}

dfs(arr: t)
print(0)
*/
