def solution(n, results):
    boxing = Boxing(n)
    boxing.fight(results)
    return boxing.get_ranked_num()

class Boxing():
    def __init__(self, n):
        self.n = n
        self.players = {}        
        # add player
        for i in range(1, n+1):
            self.players[i] = [[],[]]
    
    def fight(self, results):
        for result in results:
            win, lose = result
            winner_stronger_lst, winner_weaker_lst = self.players[win]
            loser_stronger_lst, loser_weaker_lst = self.players[lose]
            
            for winner_stronger in winner_stronger_lst:
                self.players[winner_stronger][1] = list(set(self.players[winner_stronger][1] + [lose] + self.players[lose][1]))
            self.players[win][1] = list(set(self.players[win][1] + [lose] + self.players[lose][1]))
            
            for loser_weaker in loser_weaker_lst:
                self.players[loser_weaker][0] = list(set(self.players[loser_weaker][0] + [win] + self.players[win][0]))
            self.players[lose][0] = list(set(self.players[lose][0] + [win] + self.players[win][0]))
            
            
    def get_ranked_num(self):
        count = 0
        for i in range(1, self.n+1):
            stronger_lst, weaker_lst = self.players[i]
            if len(stronger_lst + weaker_lst) == self.n -1:
                count += 1
                
        return count