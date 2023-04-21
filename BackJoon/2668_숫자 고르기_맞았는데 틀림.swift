//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/21.
//

import Foundation
// 2668 숫자 고르기 dfs 골5

// idea: key - value로 되어있으니까 처음부터 해서 value를 따라가면서 dfs를 하기?
// 사이클 생성으로 dfs가 끝나게 되면 그때 keys 와 values 를 비교해서 같다면 이걸 정답 배열에 추가하기

let n = Int(readLine()!)!
var arr: [Int] = [0]
var visited = Array(repeating: false, count: n+1)
var answers: [Int] = []

for _ in 0..<n {
    arr.append(Int(readLine()!)!)
}
// key: index, value: arr[index]
/*
func dfs(key: Int, start: Int, keys: [Int], values: [Int]) { // key: 해당 index, keys: index의 저장, values: value의 저장
    let value = arr[key]
    if visited[key] {
        if key == start && keys.count > 1 { // 시작지점과 같고 key가 비어있지 않으면
            answers.append(contentsOf: keys)
        }
        return
    }
    
    visited[key] = true
    dfs(key: value, start: start, keys: keys + [key], values: values + [value])
    visited[key] = false
}


for i in 1...n {
    if !visited[i] {
        dfs(key: i, start: i, keys: [], values: [])
    }
}

answers = Array(Set(answers)).sorted()
print(answers.count)
answers.forEach { print($0) }
*/

// 꼬였으면? 다시해보기
var cycle = Array(repeating: false, count: n+1) // 사이클이 발생한 것들의 모음
func dfs(i: Int, visited: [Bool]) {
    let value = arr[i]
   
}


for i in 1..<n {
    
}


answers = Array(Set(answers)).sorted()
print(answers.count)
answers.forEach { print($0) }
