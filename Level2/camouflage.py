# https://programmers.co.kr/learn/courses/30/lessons/42578

import itertools

def solution(clothes):
    clothes_dict = {}
    for _, pos in clothes:
        if clothes_dict.get(pos):
            clothes_dict[pos] += 1
        else:
            clothes_dict[pos] = 2
    numbers = list(clothes_dict.values())

    value = 1
    for i in range(len(numbers)):
        value *= numbers[i]
        
    return value -1