class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        ans = []
        
        max_ = 0
        
        for i in arr:
            check = set()
            skip = False
            for char_ in i:
                if char_ in check:
                    skip = True
                else:
                    check.add(char_)
            if skip == True:
                continue
            curr = [i]
            max_ =  max(max_, len(i))
            for j in ans:
                if set([char_ for char_ in i]).intersection(set([char_ for char_ in j])):
                    continue
                max_ =  max(max_, len(i+j))
                curr.append(j + i) 
            ans.extend(curr)
            
        return max_