# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    if len(number) == 1:
        return ''
        
    number = list(number)
    number.reverse()
    s = []
    while k > 0:           
        s.append(number.pop())    
        
        if len(number) <= 0:
            break
            
        if s[-1] >= number[-1]:
            continue            
        else: #s[-1] < number[-1]:
            while s[-1] < number[-1]:
                s.pop()
                k -= 1
                if k <= 0 or len(s) <= 0:
                    break
                                
    if k != 0:
        s = s[:len(s)-k]
            
    if len(s) > 0:
        s.reverse()
        number = number + s
        
    number.reverse()
    return ''.join(number)