class Solution:
    def countWords(self, nums1: List[str], nums2: List[str]) -> int:
        
        reject = set()
        cache = {}
        for i in nums1:
            if i in cache:
                cache.pop(i)
                reject.add(i)
            elif i in reject:
                continue
            else:
                cache[i] = 1
        
        cache2 = {}
        for i in nums2:
            if i in cache2:
                cache2.pop(i)
                reject.add(i)
            elif i in reject:
                continue
            else:
                cache2[i] = 1
        
        print(cache, cache2)
        
        
        res = 0
        for i in cache:
            if i in cache2:
                res += 1 
                
        return res