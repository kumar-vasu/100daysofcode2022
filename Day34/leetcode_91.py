class Solution:
    def numDecodings(self, s: str) -> int:
        
        map_ = set()
        
        for i in range(ord('A'), ord('Z') + 1):
            map_.add(str(i - ord('A') + 1))
        
        dp = {}
        
        def backtrack(string, index):
            if index in dp:
                return dp[index]
            
            if len(string) == 1:
                if string in map_:
                    return 1
                else:
                    return 0
            
            else:
                curr = 0
                curr_string = ''
                #print(string, "w")
                for i in [index, index + 1]:
                    if i >= len(string):
                        break
                    curr_string += string[i]
                    #print(curr_string, string[i+1:])
                    if curr_string in map_:
                        if i+1 < len(string):
                            curr += backtrack(string, i+1)
                        else:
                            curr += 1
            dp[index] = curr
            return curr
        
        if s == '':
            return 0 
        
        ways = backtrack(s, 0)
        
        return ways