//
//  main.swift
//  BackJoon
//
//  Created by kokojong on 2023/04/27.
//

import Foundation
// 백준 2343 기타 레슨 실1
/*
let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let n = input[0]
let m = input[1]

let arr = readLine()!.split(separator: " ").map { Int(String($0))! }
let maxV = arr.reduce(0, +)
var answers: [Int] = []
/*
func binarySearch(l: Int, r: Int) {
    let mid = (l + r) / 2 // 블루레이의 크기
    if mid == l { return } // 종료
    
    var cnt = 0 // 블루레이의 갯수 (m과 같아야함)
    var sum = 0 // 하나의 블루레이에 들어간 크기 합
    
    for a in arr {
        if sum + a > mid { // 넘친다면
            sum = a // sum 초기화(새로운 것 넣어줌)
            cnt += 1 // cnt += 1
        } else {
            sum += a
        }
    }
    if sum > 0 { cnt += 1 } // 남은거 털기
    
    if cnt > m { // 크기를 너무 작게 잡은 경우 -> cnt가 많아짐
        binarySearch(l: mid, r: r)
    } else if cnt == m {
        answers.append(mid)
        binarySearch(l: l, r: mid) // 혹시 더 작은 경우가 있나 찾기
    } else { // 크기를 너무 크게 잡은 경우 -> cnt가 적어짐
        binarySearch(l: l, r: mid)
    }
} */

func binarySearch(l: Int, r: Int) {
    var l = l
    var r = r
    
    while l < r {
        let mid = (l + r) / 2 // 블루레이의 크기
        
        var cnt = 0 // 블루레이의 갯수 (m과 같아야함)
        var sum = 0 // 하나의 블루레이에 들어간 크기 합
        
        for a in arr {
            if sum + a > mid { // 넘친다면
                sum = a // sum 초기화(새로운 것 넣어줌)
                cnt += 1 // cnt += 1
            } else {
                sum += a
            }
        }
        if sum > 0 { cnt += 1 } // 남은거 털기
        
        if cnt > m { // 크기를 너무 작게 잡은 경우 -> cnt가 많아짐
            l = mid + 1
        } else if cnt == m {
            answers.append(mid)
            r = mid // 혹시 더 작은 경우가 있나 찾기
        } else { // 크기를 너무 크게 잡은 경우 -> cnt가 적어짐
            r = mid
        }
    }
    
    print(answers.min()!)
        
}

binarySearch(l: arr.max()!, r: maxV) // 제일 큰 크기보다 작은 조각으로는 쪼갤 수 없음, 다 더한것의 크기 이하여야함.
*/
