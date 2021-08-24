# https://programmers.co.kr/learn/courses/30/lessons/49189

def solution(n, edge):
    answer = 0
    graph = Graph()
    for e in edge:
        graph.add_edge(e)
    max_level = graph.calc_level()
    
    for i in range(1, len(graph.leaves.keys())+1):
        if graph.leaves[i].level == max_level:
            answer += 1
    
    return answer


class Node():
    def __init__(self, num):
        self.num = num
        self.edges = [] 
        self.level = -1        
        
class Graph():
    def __init__(self):
        self.leaves = { 1 : Node(1) }
        self.leaves_count = 1
        
        
    def add_edge(self, edge):
        n1, n2 = edge
        if not n1 in self.leaves.keys():
            self.leaves[n1] = Node(n1)
            self.leaves_count += 1
            
        if not n2 in self.leaves.keys():
            self.leaves[n2] = Node(n2)
            self.leaves_count += 1
            
        self.leaves[n1].edges.append(n2)
        self.leaves[n2].edges.append(n1)
        
    def calc_level(self):
        level = 0
        finish  = []
        count = 0
        
        self.leaves[1].level = level
        next_leaves_num = self.leaves[1].edges
        count += 1
        finish.append(self.leaves[1].num)
        
        while self.leaves_count > count:
            level += 1
            tmp_next = []        
            for next_leaf_num in next_leaves_num:
                if self.leaves[next_leaf_num].level == -1:
                    self.leaves[next_leaf_num].level = level
                    if not next_leaf_num in finish:
                        tmp_next += self.leaves[next_leaf_num].edges
                    count += 1
                    finish.append(next_leaf_num)
                    
            next_leaves_num = list(set(tmp_next))
                        
        return level