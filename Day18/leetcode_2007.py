class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        double = []
        single = []
        if len(changed) % 2 == 1:
            return []
        changed = sorted(changed)
        zeroes = 0
        singles = {}
        
        for i in changed:
            if i == 0:
                if zeroes == 1:
                    double.append(0)
                    zeroes = 0
                else:
                    single.append(0)
                    zeroes = 1
            elif i/2 in single and singles[i/2] > 0:
                double.append(i)
                singles[i/2] -= 1
            else:
                if i in singles:
                    singles[i] += 1
                else:
                    singles[i] = 1
                single.append(i)
                
        if len(single) == len(double):
            return single
        else:
            return []
        