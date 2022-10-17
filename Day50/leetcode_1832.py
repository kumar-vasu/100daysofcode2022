class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = set(list(string.ascii_lowercase))
        
        for i in range(len(sentence)):
            if sentence[i] in alphabets:
                alphabets.remove(sentence[i])
       
        if len(alphabets) == 0:
            return True
        else:
            return False
            