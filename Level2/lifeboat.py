# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    
    people.sort()
    max_idx = len(people) - 1
    min_idx = 0
    while max_idx > min_idx:
        if people[max_idx] + people[min_idx] > limit:
            answer += 1
            max_idx -= 1
        else:
            answer += 1
            max_idx -= 1
            min_idx += 1
        
    if max_idx == min_idx:
        answer += 1
            
                   
        
    return answer