class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties = list(reversed(sorted(properties, key = lambda x:[x[0],-x[1]])))
        
        weak = 0
        
        at = properties[0][0]
        de = properties[0][1]
        
        
        for i in range(1, len(properties)):
            
            if properties[i][1] < de and properties[i][0] < at:
                weak += 1
            if properties[i][1] > de:
                at = properties[i][0]
                de = properties[i][1]
        
        return weak