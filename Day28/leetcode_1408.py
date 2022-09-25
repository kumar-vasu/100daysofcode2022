import copy
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set() 
        s_list = copy.deepcopy(words) 
        for word in words:
            s_list.remove(word)
            for word2 in s_list:
                if word in word2:
                    res.add(word)
            s_list.append(word)    
        return list(res)