# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = n
    
    lost_and_reserve = []
    # lost and reserve    
    for lost_num in lost:   
        if reserve.count(lost_num):
            lost_and_reserve.append(lost_num)
            
    lost_ = list(set(lost) - set(reserve)) 
    reserve = list(set(reserve) - set(lost))
    print(lost_)
    print(reserve)
    answer -= len(lost_)
    for lost_num in lost_:
        for idx in range(len(reserve)):
            if (lost_num - reserve[idx])**2 <= 1:
                reserve.pop(idx)
                answer += 1
                break
                
    return answer