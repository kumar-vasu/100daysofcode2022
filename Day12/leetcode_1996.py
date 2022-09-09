class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        properties = list(reversed(sorted(properties, key = lambda x:x[0])))
        
        weak = 0
        
        at = properties[0][0]
        de = properties[0][1]
        
        for i in range(1, len(properties)):
            if properties[i][0] < at and properties[i][1] < de:
                weak += 1
            else:
                at = properties[i][0]
                de = properties[i][1]
        
        return weak