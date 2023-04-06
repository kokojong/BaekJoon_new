//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/06.
//

import Foundation
// 17615 볼 모으기 그리디 실1
/*
let n = Int(readLine()!) ?? 0
let arr = Array(readLine()!)

let redCnt = arr.filter { $0 == "R"}.count
let blueCnt = arr.filter { $0 == "B" }.count

// idea: R..B...B 또는 B...R...R 두가지 중 하나다.
// -> R를 왼쪽 or 오른쪽에 몰아넣음, B를 왼쪽 or 오른쪽으로 몰아넣음

func redToLeft() -> Int {
    // 첫 뭉탱이 R은 제외하고 뒤에 나오는 R의 갯수를 세어준다.
    var cnt = 0
    var arr = arr
    if arr.first! == "R" {
        for i in arr.firstIndex(of: "B")!..<n {
            if arr[i] == "R" { cnt += 1}
        }
    } else {
        cnt = arr.filter { $0 == "R" }.count
    }
    return cnt
}

func redToRight() -> Int {
    // 첫 뭉탱이 R은 제외하고 뒤에 나오는 R의 갯수를 세어준다.
    var cnt = 0
    var arr = arr
    arr.reverse()
    if arr.first! == "R" {
        for i in arr.firstIndex(of: "B")!..<n {
            if arr[i] == "R" { cnt += 1 }
        }
    } else {
        cnt = arr.filter { $0 == "R" }.count
    }
    return cnt
}

func blueToLeft() -> Int {
    // 첫 뭉탱이 B은 제외하고 뒤에 나오는 B의 갯수를 세어준다.
    var cnt = 0
    if arr.first! == "B" {
        for i in arr.firstIndex(of: "R")!..<n {
            if arr[i] == "B" { cnt += 1}
        }
    } else {
        cnt = arr.filter { $0 == "B" }.count
    }
    return cnt
}

func blueToRight() -> Int {
    // 첫 뭉탱이 B은 제외하고 뒤에 나오는 B의 갯수를 세어준다.
    var cnt = 0
    var arr = arr
    arr.reverse()
    if arr.first! == "B" {
        for i in arr.firstIndex(of: "R")!..<n {
            if arr[i] == "B" { cnt += 1}
        }
    } else {
        cnt = arr.filter { $0 == "B" }.count
    }
    return cnt
}

func solution() -> Int {
    return min(redToLeft(), redToRight(), blueToLeft(), blueToRight())
}

if arr.count <= 2 || redCnt == n || blueCnt == n {
    print(0)
} else {
    print(solution())
}
*/
