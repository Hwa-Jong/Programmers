# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0
    doc_num = len(priorities)
    
    while True:
        doc = priorities.pop(0)
        location -= 1
        
        #last doc
        if len(priorities) == 0:
            return answer+1
                
        if doc < max(priorities):
            priorities.append(doc)
            if location == -1:
                location = doc_num-1
                
        else:
            answer += 1
            if location == -1:
                return answer
            doc_num -= 1
            