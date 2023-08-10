//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/21.
//

import Foundation
// 2668 숫자 고르기 dfs 골5

// idea: key - value로 되어있으니까 처음부터 해서 value를 따라가면서 dfs를 하기?
// dfs가 끝나게 되면 그때 keys 와 values 를 비교해서 같다면 이걸 정답 배열에 추가하기

// 어이없는게 dfs를 실행하는 부분에서 1..<n으로 했다...으어ㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓㅓ

/*
let n = Int(readLine()!)!
var arr: [Int] = [0]
var answers: [Int] = []

for _ in 0..<n {
    arr.append(Int(readLine()!)!)
}
// key: index, value: arr[index]

func dfs(key: Int, keys: [Int], values: [Int]) { // key: 해당 index, keys: index의 저장, values: value의 저장
    let value = arr[key]
    if keys.contains(key) { // 이미 있는 키라면
        if Set(keys) == Set(values) {
            answers.append(contentsOf: keys)
        }
        return
    }
    
    var values = values
    values.append(value)
    var keys = keys
    keys.append(key)
    
    dfs(key: value, keys: keys, values: values)
}


for i in 1...n {
    if !answers.contains(i) {
        dfs(key: arr[i], keys: [i], values: [arr[i]])
    }
}

print(answers.count)
answers.sorted().forEach {
    print($0)
}
/*
