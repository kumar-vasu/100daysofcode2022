class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        dp = {}
        
        def backtrack(die, target):
            
            if str(die)+"|"+str(target) in dp:
                return dp[str(die)+"|"+str(target)]
            
            if die == 0 and target != 0 or die != 0 and target == 0:
                dp[str(die)+"|"+str(target)] = 0
                return 0
            elif die == 0 and target == 0:
                dp[str(die)+"|"+str(target)] = 1
                return 1
            
            ways = 0
            
            for i in range(1, k+1):
                if i <= target:
                    ways += backtrack(die-1, target-i)
                #print(i, ways, die)
                
            dp[str(die)+"|"+str(target)] = ways
            
            return ways
        
        ways = backtrack(n, target)
        #print(ways % 10**9)
        return ways % (10**9 + 7)