class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        dict_ = {}
        for num in arr:
            if abs(num - x) in dict_:
                dict_[abs(num - x)].append(num)
            else:
                dict_[abs(num - x)] = [num]
                
        keys = sorted(dict_.keys())
        res = []
        
        stack = []
        while k != 0:
            
            stack = sorted(dict_[keys.pop(0)])
            len_ = len(stack)

            for i in range(len_):
                res.append(stack.pop(0))
                
                k -= 1
                if k == 0:
                    break
                    
        return sorted(res)