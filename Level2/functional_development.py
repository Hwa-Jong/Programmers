# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    
    progresses_num = len(progresses)
    state = 0
    
    while True:
        date = ceil((100 - progresses[state]) / speeds[state])
        
        count = 1
        for idx in range(state + 1, progresses_num):
            if progresses[idx] + date*speeds[idx] >= 100:
                count += 1
            else:
                break
                
        answer.append(count)
        state += count
        
        if state >= progresses_num:
            break
        
    return answer 

def ceil(value):
    if value % 1.0 == 0.0:
        return int(value)
    return int(value + 1)
        
    