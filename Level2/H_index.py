# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    
    for idx in range(len(citations)):
        if citations[idx] < idx+1:
            answer = idx
            break
            
        if len(citations) -1 == idx:
            answer = idx+1
            
    return answer