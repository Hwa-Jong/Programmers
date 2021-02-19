# https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq

def solution(jobs):
    answer = 0
    
    wait = []
    jobs_rev = sorted(jobs, key=lambda x:x[0], reverse=True)
    
    act_time = 0    
    now_time = 0
    while len(jobs_rev) >= 1:
        if jobs_rev[-1][0] <= now_time:
            job = jobs_rev.pop()
            heapq.heappush(wait, (job[1], job[0]))
            
        else:
            if len(wait) == 0:
                now_time += 1
            else:
                job_length, start_time = heapq.heappop(wait)
                now_time += job_length 
                act_time += (now_time - start_time)
                
    while len(wait) >= 1:
        job_length, start_time = heapq.heappop(wait)
        now_time += job_length 
        act_time += (now_time - start_time)
    
    return act_time // len(jobs)