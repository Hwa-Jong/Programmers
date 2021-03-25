# https://programmers.co.kr/learn/courses/30/lessons/42861

def solution(n, costs):
    answer = 0
    group = [-1 for i in range(n)]
    group_num = -1
    costs.sort(reverse=True, key=lambda x:x[2])
    
    while len(costs) >= 1:
        island1, island2, cost = costs.pop()
        if group[island1] == -1 and group[island2] == -1:
            group_num += 1
            group[island1] = group_num
            group[island2] = group_num
            answer += cost
            
        elif group[island1] == -1 or group[island2] == -1:
            now_group = max(group[island1], group[island2])
            group[island1] = now_group
            group[island2] = now_group
            answer += cost
            
        elif group[island1] != group[island2]:
            now_group = min(group[island1], group[island2])
            merge_group = max(group[island1], group[island2])
            answer += cost
            for i in range(n):
                if group[i] == merge_group:
                    group[i] = now_group
        
        if len(set(group)) == 1:
            break
            
    return answer