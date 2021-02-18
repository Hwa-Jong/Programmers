def solution(participant, completion):
    
    names = set(participant)
    
    players = {name:0 for name in names}
    
    for name in participant:
        players[name] += 1
        
    for name in completion:
        players[name] -= 1
        if players[name] == 0:
            del players[name]
        
    answer = list(players)
        
    return answer[0]