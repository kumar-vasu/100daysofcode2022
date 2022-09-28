class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:

        lined_stones = sorted([a,b,c])
        print(lined_stones, "2")
        end_stones = [lined_stones[0], lined_stones[-1]]

        len_ = end_stones[1] - end_stones[0] + 1
        maxsteps = lined_stones[2] - lined_stones[0] - 2
        
        if len_ == 3:
            minsteps = 0
        elif (lined_stones[2] - lined_stones[1] + 1 <= 3) or (lined_stones[1] - lined_stones[0] + 1 <= 3):
            minsteps = 1
        else:
            minsteps = 2
            
        return [minsteps, maxsteps]
