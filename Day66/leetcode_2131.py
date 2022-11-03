class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        reserve = {}
        result = 0
        
        for word in words:
            if "".join(list(reversed(word))) in reserve:
                reserve["".join(list(reversed(word)))] -= 1
                if reserve["".join(list(reversed(word)))] == 0:
                    del reserve["".join(list(reversed(word)))]
                result += 4
            else:
                if word in reserve:
                    reserve[word] += 1
                else:
                    reserve[word] = 1
            #print(reserve, word, result)
       
        for i in reserve:
            if i[0] == i[1]:
                result += 2
                break
        #print(reserve)
        return result