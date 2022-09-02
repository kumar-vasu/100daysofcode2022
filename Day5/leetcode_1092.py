class Solution:
    def shortestCommonSupersequence(self, text1: str, text2: str) -> str:
        
        dp = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                
                if i == 0  or j == 0:
                    continue
                
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        i = len(dp)-1
        j = len(dp[0])-1

        result = []
        while i > 0 and j > 0:
            if dp[i][j] == 0:
                break
            if dp[i][j-1] == dp[i-1][j-1] and dp[i-1][j] == dp[i-1][j-1]:
                if dp[i][j] > dp[i-1][j-1]:
                    result.append(text2[i-1])
                    i = i-1
                    j = j-1
                    continue
                else:
                    i = i
                    j = j-1
                    continue
            if dp[i][j-1] > dp[i-1][j-1]:
                j = j-1
                continue
            if dp[i-1][j] > dp[i-1][j-1]:
                i -= 1
                continue
            else:
                i-=1
                j-=1
                continue
        result = [i for i in reversed(result)]
        
        p1 = 0
        p2 = 0
        p3 = 0
        
        final = []
        
        while p3 < len(result):
            if p1 < len(text1) and text1[p1] == result[p3] and p2 < len(text2) and text2[p2] == result[p3]:
                final.append(result[p3])
                p1 += 1
                p2 += 1
                p3 += 1
                continue
            while p1 < len(text1) and text1[p1] != result[p3]:
                print(2, "p1", p1)
                final.append(text1[p1])
                p1 += 1
            while p2 < len(text2) and text2[p2] != result[p3]:
                print(3, "p2", p2)
                final.append(text2[p2])
                p2 += 1
        if p3 == len(result) and p2 < (len(text2)):
            final.extend([i for i in text2[p2:]])
        
        if p3 == len(result) and p1< (len(text1)):
            final.extend([i for i in text1[p1:]])
            
        return "".join(final)
                    
                
        