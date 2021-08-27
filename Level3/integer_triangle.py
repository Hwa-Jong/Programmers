# https://programmers.co.kr/learn/courses/30/lessons/43105
def solution(triangle):
    answer = 0
    t = calc_sum_triangle(triangle)
    answer = max(t[-1])
    return answer

def calc_sum_triangle(triangle):
    for level in range(1, len(triangle)):
        for idx in range(len(triangle[level])):
            up_left = idx - 1
            up_right = idx
            
            if up_left < 0:
                triangle[level][idx] += triangle[level-1][up_right]
            elif up_right >= len(triangle[level-1]):
                triangle[level][idx] += triangle[level-1][up_left]
                
            else:
                max_val = max(triangle[level-1][up_right], triangle[level-1][up_left])
                triangle[level][idx] +=max_val
            
    return triangle