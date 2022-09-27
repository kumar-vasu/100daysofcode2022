class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dt = {'2':["a","b","c"], '3':["d","e","f"], '4':["g","h","i"],
              '5':["j","k","l"], '6':["m","n","o"], '7':["p","q","r", "s"],
              '8':["t","u","v"], '9':["w","x","y","z"]}
        
        if digits == '': 
            return None
     
        cur_mix = dt[digits[0]]
        
        i = 1
        
        while i < len(digits):
            temp_mix = [] 
            
            for m in cur_mix: 
                for n in dt[digits[i]]:
                    temp_mix.append(m+n)
            
            cur_mix =temp_mix 
            
            i += 1 
        
        return cur_mix
            