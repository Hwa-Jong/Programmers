#https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    answer = 0
    name_length = len(name)
    move = [1 if name[i]=='A' else 0 for i in range(name_length)]
    
    for i in range(name_length):
        now_str = name[i]
        answer += get_move_num_alphabet(now_str, 'A')
        
    answer += get_move_num_cursor(move)
    
    return answer

def get_move_num_alphabet(str1, str2):
    return min(abs(ord(str1) - ord(str2)), 26 - abs(ord(str1) - ord(str2)))

def get_move_num_cursor(move):
    cursor_pos = 0
    move_num = 0
    move[cursor_pos] = 1
    
    while sum(move) != len(move):
        now_move = [move[i%len(move)] for i in range(cursor_pos, len(move)+cursor_pos)]    
        move_right = now_move[1:][:(len(move)-1)//2]
        move_left = now_move[1:][::-1][:(len(move)-1)//2] 
        
        is_right_direction = check_direction(move_right, move_left)
        if is_right_direction:
            cursor_pos += 1
        else:
            cursor_pos -= 1
            
        move_num += 1
        move[cursor_pos] = 1
        
    return move_num
    

def check_direction(right, left):
    assert len(right) == len(left), "len(right) == len(left) but differnt"
    
    right_direction = True
    left_direction = False
    
    for i in range(len(right)):
        r = right[i]
        l = left[i]
        if r == 0 and l == 1:
            return right_direction
        elif r == 1 and l == 0:
            return left_direction
        
        elif r == 0 and l == 0:
            for j in range(i+1, len(right)):
                r_ = right[j]
                l_ = left[j]
                if r_ == 1 and l_ == 0:
                    return right_direction
                elif r_ == 0 and l_ == 1:
                    return left_direction
                
            return right_direction