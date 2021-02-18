# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    length = len(prices)
    for i in range(length):
        now_value = prices[i]
        for j in range(i+1, length):
            if prices[j] < now_value or j == length -1:
                answer.append(j-i)
                break
    answer.append(0)
    return answer