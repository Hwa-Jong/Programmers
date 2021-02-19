# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        make_new_food(scoville)
        answer += 1
            
    return answer

def make_new_food(heap):
    first_low_scov = heapq.heappop(heap)
    second_low_scov = heapq.heappop(heap)
    
    # append new food scoville
    heapq.heappush(heap,first_low_scov + second_low_scov * 2)