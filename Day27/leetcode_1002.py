class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cache = {}
        
        for j in range(len(words[0])):
            if words[0][j] in cache:
                cache[words[0][j]] += 1
            else:
                cache[words[0][j]] = 1
        
        
        for i in range(1, len(words)):
            cache_new = {}
            for j in range(len(words[i])):
                if words[i][j] in cache :
                    if words[i][j] in cache_new:
                        cache_new[words[i][j]] += 1
                    else:
                        cache_new[words[i][j]] = 1
                    cache[words[i][j]] -= 1
                    if cache[words[i][j]] == 0:
                        cache.pop(words[i][j])
            cache = cache_new
        
        res = []
        for i in cache_new:
            res.extend([i]*cache[i])
        
        return res