# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ''
    numbers_str = [[str(x), len(str(x))] for x in numbers]
    numbers_sorted = []
    for num, length in numbers_str:
        num = num*4
        numbers_sorted.append([num[:4], length])    
        
    numbers_sorted.sort(reverse = True, key=lambda x:x[0])
    
    for num, length in numbers_sorted:
        answer += num[:length]
        
    if int(answer) == 0:
        answer = '0'
    
    return answer

    