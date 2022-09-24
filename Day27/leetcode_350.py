class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        cache = {}
        for i in nums1:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1
                
        res = []
        for i in nums2:
            if i in cache:
                cache[i] -= 1
                if cache[i] == 0:
                    cache.pop(i)
                res.append(i)
                
        return res
        
        