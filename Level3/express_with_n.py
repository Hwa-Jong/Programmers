# https://programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):    
    
    table = get_number_table(N)
    
    return is_include(table, number)
    

def get_nnn(n, r):
    n = str(n)
    s = ''
    for i in range(r):
        s += n        
    return int(s)

def is_include(table, number):
    if number in table[0]:
        for i in range(1,9):
            if number in table[i]:
                return i
        
    return -1


def get_number_table(number):
    # index 0 == all number, index 1~8 == # of number
    table = [[] for _ in range(9)]
    
    table = my_append(table, number, idx=1)
    
    for i in range(2, 9):
        table = my_append(table, get_nnn(number, i), idx=i)
    
        a = 1
        b = i-1
        while True:
            if a  > b:
                break
            table = get_can_make(table, a, b, i)
            a += 1
            b -= 1
    
    
    return table
            
def get_can_make(table, a, b, append_idx):
    lst1 = table[a]
    lst2 = table[b]
    
    for n1 in lst1:
        for n2 in lst2:
            table = my_append(table, n1+n2, append_idx)
            table = my_append(table, n1-n2, append_idx)
            table = my_append(table, n2-n1, append_idx)
            table = my_append(table, n1*n2, append_idx)
            table = my_append(table, n1//n2, append_idx)
            table = my_append(table, n2//n1, append_idx)
            
    return table
        
    
def my_append(lst, n, idx):
    if n in lst[0] or n <= 0:
        return lst
    
    lst[0].append(n)
    lst[idx].append(n)
    return lst