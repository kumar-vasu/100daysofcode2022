class Solution:
    
    def addRest(self, list1, list2):
        res = ""
        while len(list1) > 0 or len(list2) > 0:
            res += list1.pop(0)
            res += list2.pop(0)
        return res
    
    def reformat(self, s: str) -> str:
        numbers = []
        alphabets = []
        
        for i in s:
            if ord(i) <= 57 and ord(i) >= 48:
                numbers.append(i)
            else:
                alphabets.append(i)
        
        if abs(len(numbers) - len(alphabets)) > 1:
            return ""
        
        print(numbers, alphabets)
        res = ""
        if len(numbers) > len(alphabets):
            res += numbers.pop(0)
            res += self.addRest(alphabets, numbers)
        elif len(numbers) < len(alphabets):
            res += alphabets.pop(0)
            res += self.addRest(numbers, alphabets)
        else:
            res = self.addRest(alphabets, numbers)
                
        return res