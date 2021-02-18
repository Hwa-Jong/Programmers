# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):    
    
    prefixs = phone_book    
    for string in phone_book:
        for prefix in prefixs:
            if prefix != string and string.startswith(prefix):
                return False
        
        
    return True