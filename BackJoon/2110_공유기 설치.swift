//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/28.
//

import Foundation
// 2110 공유기 설치 이분탐색 골4

// idea: 공유기의 거리를 이진탐색으로 구하고 c와 같다면 답으로 인정
/
let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0] // 집의 갯수
let c = input[1] // 공유기의 갯수
// 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치 -> 제일 붙어있는 애들끼리의 크기가 제일 크도록
// 즉, 처음에 설치를 하고 남은 갯수는 그 집들 사이에 두되 제일 붙어있는 공유기의 거리가 멀도록 한다(서로 멀게 배치한다)
// 문제 이해가 조금 어려버따...

var arr: [Int] = []
for _ in 0..<n {
    arr.append(Int(readLine()!)!)
}
arr.sort()

var answer = 0

var l = 1 // 가장 작은 거리 1
var r = arr.last! - arr.first! // 가장 긴 거리 - 처음이랑 끝 사이의 거리

func binarySearch() {
    while l <= r {
        let mid = (l + r) / 2 // 공유기와 공유기 사이의 거리
        
        var x = arr.first! // 첫 위치로 시작
        var cnt = 1 // 공유기의 갯수 - 시작점에 놓으니까 1
        
        for i in 1..<n {
            if arr[i] >= x + mid { // 다음 공유기는 현재 위치 + 공유기 거리 보다 크거나 같아야한다.
                cnt += 1
                x = arr[i] // arr[i]에 공유기 설치
            }
        }
        
        if cnt > c { // 많이 설치된 경우 -> mid 를 더 크게 가져가야함
            l = mid + 1
            answer = max(answer, mid)
        } else if cnt == c { // 알맞게 설치 된 경우 answer에 포함하되 더 큰 값이 있을 수 있어 left를 조정
            l = mid + 1
            answer = max(answer, mid)
        } else { // 너무 적게 설치된 경우
            r = mid - 1
        }
    }
    print(answer)
}

binarySearch()
