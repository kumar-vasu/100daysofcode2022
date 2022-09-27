class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list('L' + dominoes + 'R')
        
        i, j = 0, 1
        while j < len(dominoes):
            if dominoes[j] == '.': 
                j += 1
                continue
                
            if dominoes[i] == 'L' and dominoes[j] == 'L':
                for k in range(i + 1, j): dominoes[k] = 'L'
            elif dominoes[i] == 'R' and dominoes[j] == 'R':
                for k in range(i + 1, j): dominoes[k] = 'R'
            
            elif dominoes[i] == 'R' and dominoes[j] == 'L':
                ii, jj = i + 1, j - 1
                while ii < jj:
                    dominoes[ii] = 'R'
                    dominoes[jj] = 'L'
                    ii += 1
                    jj -= 1
                    
            i, j = j, j + 1
        
        return ''.join(dominoes[1: -1])