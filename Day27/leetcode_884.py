class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        reject =set()
        cache = set()
        
        l1 = s1.split(" ")
        for i in l1:
            if i in cache:
                cache.remove(i)
                reject.add(i)
            elif i in reject:
                continue
            else:
                cache.add(i)
        
        reject2 =set()
        cache2 = set()
        l2 = s2.split(" ")
        for i in l2:
            if i in cache2:
                cache2.remove(i)
                reject2.add(i)
            elif i in reject2:
                continue
            else:
                cache2.add(i)
        
        res = (cache - (cache.intersection(cache2)) - reject2).union(cache2 - (cache.intersection(cache2)) - reject)
        
        return res