//
//  main.swift
//  CommandLine
//
//  Created by kokojong on 3/30/24.
//

import Foundation

// 화면에 있는거를 모두 복사해서 저장
// 붙여넣기
// 하나를 삭제

let S = Int(readLine()!)!

var queue = [[1, 0, 0]] // 현재, 클립보드, 시간
var visited = Array(repeating: Array(repeating: false, count: 2001), count: 2001) // 최대한으로 해두기
visited[1][0] = true

var idx = 0 // queue의 인덱스로 활용

while idx < queue.count {
    let now = queue[idx][0]
    let clip = queue[idx][1]
    let time = queue[idx][2]
    
    if now == S {
        print(time)
        break
    }
    if now > 0 && now <= 2000 && !visited[now][now] { // 복사하기(클립보드 덮어쓰기)
        visited[now][now] = true
        queue.append([now, now, time+1])
    }
    
    if clip > 0 && now+clip <= 2000 && !visited[now][now+clip] { // 클립보드 내용 추가하기, 클립보드는 유지
        visited[now+clip][clip] = true
        queue.append([now+clip, clip, time+1])
    }
    
    if now > 0 && now <= 2000 && !visited[now-1][clip] {
        visited[now-1][clip] = true
        queue.append([now-1, clip, time+1])
    }
    
    idx += 1
}

