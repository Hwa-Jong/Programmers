# https://programmers.co.kr/learn/courses/30/lessons/42628

def solution(operations):
    Q = []
    for idx, oper in enumerate(operations):
        op, value = oper.split()
        if op == 'I':
            Q.append(int(value))
        else: # op == 'D'
            if len(Q) == 0:
                continue
            elif value == '-1':
                Q.sort(reverse=True)
                Q.pop()
            else: # value == '1'
                Q.sort()
                Q.pop()
                
    if len(Q) == 0:
        v_max = 0
        v_min = 0
    else:
        v_max = max(Q)
        v_min = min(Q)
    answer = [v_max, v_min]
    return answer