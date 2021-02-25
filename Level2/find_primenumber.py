# https://programmers.co.kr/learn/courses/30/lessons/42839

import itertools 

def solution(numbers):
    answer = 0
    numbers = [numbers[i] for i in range(len(numbers))]
    all_permutations = []
    for i in range(1, len(numbers)+1):
        permutation = list(set(itertools.permutations(numbers, i)))
        for num in permutation:
            number = ''
            for n in num:
                number += n
            all_permutations.append(int(number))
            
    all_permutations = list(set(all_permutations))
    for num in all_permutations:
        if is_prime_num(num):
            answer += 1
    
    return answer


def is_prime_num(num):
    if num <= 1:
        return False    
    if num == 2:
        return True    
    if num % 2 == 0:
        return False
    
    n = 3
    while n < num:
        if num % n == 0:
            return False
        n += 2
    return True