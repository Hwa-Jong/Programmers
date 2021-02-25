# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    # min = 3x3
    row_base , col_base = 3, 3
    
    brown_tmp = ((brown + 2)//2) + 1
    remain = brown_tmp - row_base - col_base
    for r in range(remain):
        col = col_base + remain - r
        row = col_base + r
        
        pred_yellow = row*col - brown
        if pred_yellow==yellow:
            return [col, row]

    return [col_base, row_base]