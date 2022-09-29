class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
                
        types = len(set(candyType))

        if types >= len(candyType)//2:
            return len(candyType)//2
        else:
            return types