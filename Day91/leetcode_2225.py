class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners  = set()
        almost_losers = set()
        losers = set()
        
        for winner, loser in matches:
            if winner not in losers and winner not in almost_losers:
                winners.add(winner)
            if loser not in winners and loser not in almost_losers and loser not in losers:
                almost_losers.add(loser)
            elif loser in winners:
                winners.remove(loser)
                almost_losers.add(loser)
            elif loser in almost_losers:
                almost_losers.remove(loser)
                losers.add(loser)
            else:
                losers.add(loser)
            #print(winners, almost_losers, losers)
        res = [sorted(list(winners)), sorted(list(almost_losers))]
        
        return res