# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for idx in range(len(commands)):   
        i, j, k = commands[idx]
        values = array[i-1:j]
        values.sort()
        v = values[k-1]
        answer.append(v)     
    return answer