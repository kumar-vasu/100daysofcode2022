class Solution:
    def is_palindrome(self, string):
        for i in range(len(string)//2):
            if string[i] != string[len(string) - i - 1]:
                return False
        return True
    
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        odds_dict = {}
        for word in words:
            odds_dict[word] = set()
        
        for word in words:
            for j in range(len(word)):
                if word[j] in odds_dict[word]:
                    odds_dict[word].remove(word[j])
                else:
                    odds_dict[word].add(word[j])
        
        output = []
        for i in range(1, len(words)):
            #print(i, odds_dict[words[i]])
            for j in range(i):
                #print(j, odds_dict[words[j]])
                union = odds_dict[words[i]].union(odds_dict[words[j]])
                intersection = odds_dict[words[i]].intersection(odds_dict[words[j]])
                if len(union - intersection) <= 1:
                    if self.is_palindrome(words[i]+words[j]):
                        output.append([i, j])
                    if self.is_palindrome(words[j]+words[i]):
                        output.append([j, i])                    
        return output
                    