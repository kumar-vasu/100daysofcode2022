class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        
        # init values
        result = ""
        p1 = 0
        p2 = 0
        l1 = len(word1)
        l2 = len(word2)
        
        # iteration over both pointers, while both words
        # have letters
        while p1 < l1 and p2 < l2:
            
            # easy case where current word1 letter is bigger
            if word1[p1] > word2[p2]:
                result += word1[p1]
                p1 += 1
                
            # easy case where current word2 letter is bigger
            elif word1[p1] < word2[p2]:
                result += word2[p2]
                p2 += 1
                
            # as soon as words are equal we need to figure out
            # how to go on. We do that by looking where we can
            # get the next most highest letter
            else:
                if word1[p1:] > word2[p2:]:
                    result += word1[p1]
                    p1 += 1
                else:
                    result += word2[p2]
                    p2 += 1
        
        # add the rest of the words (one of them will be empty!)
        result += word1[p1:] + word2[p2:]
        
        return result