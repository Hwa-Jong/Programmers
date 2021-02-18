#  https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    answer = 0
    status = []
    cross = []    
    idx = 0
    total_truck_num = len(truck_weights)
    while True:
        #break
        if idx >= total_truck_num:
            answer += bridge_length
            break
                
        #out
        if len(status) > 0 and status[0] <= answer:  
            status.pop(0)
            cross.pop(0)
            
        #next truck 
        next_truck_weight = truck_weights[idx]
        
        #in
        now_bridge_weight = sum(cross)
        if now_bridge_weight + next_truck_weight <= weight:
            cross.append(next_truck_weight)
            status.append(answer + bridge_length)
            idx += 1

        answer += 1       
    return answer