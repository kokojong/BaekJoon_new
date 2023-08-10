//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/29.
//

import Foundation
// 1654 랜선 자르기 이분탐색 실2
/*
let kn = readLine()!.split(separator: " ").map { Int(String($0))! }
let k = kn[0]
let n = kn[1] // 만들려는 수

var arr: [Int] = []
for _ in 0..<k {
    arr.append(Int(readLine()!)!)
}
let maxV = arr.max()!

var answer = 0
// N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오
var l = 1
var r = maxV

func binarySearch() {
    while l <= r {
        let mid = (l+r) / 2
        var cnt = 0
        
        for a in arr {
            cnt += a/mid // mid길이로 만들수 있는 개수
        }
        
        if cnt >= n {
            l = mid + 1
            answer = max(answer, mid)
        } else { // n보다 적은 갯수 -> mid를 줄여야함
            r = mid - 1
        }
    }
    
    print(answer)
}

binarySearch()
*/
