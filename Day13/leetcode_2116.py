class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        N = len(s)
        if ( N%2 == 1):
            return False

        max_ = 0
        min_ = 0

        for i in range(N):
            if (locked[i] == '1'):
                if (s[i] == '(' ):
                    min_ += 1
                    max_ += 1
                else:
                    min_ -= 1
                    max_ -= 1
                    if (max_ < 0):
                        return False

            else:
                max_ += 1
                min_ -= 1
            min_= max(0,min_)
        if (max_ >=0 and min_ <=0):
            return True 
        else:
            return False
                
            