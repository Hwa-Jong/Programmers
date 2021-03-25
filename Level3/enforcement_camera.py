# https://programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    camera = None
    while len(routes) >= 1:
        start, end = routes.pop()
        if camera is None:
            camera = start
            answer += 1
            continue
        elif camera < start:
            camera = start
        elif camera > end:
            routes.append([start, end])
            camera = None
            
        
    
    return answer