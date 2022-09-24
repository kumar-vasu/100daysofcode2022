class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
		
        arr = [x for x in range(100, 1000, 2)]
        d = {} #counter
        ans = []
        
        for x in digits:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
                
        for x in arr:
            s = str(x)
            a, b, c = int(s[0]), int(s[1]), int(s[2])

            if len({a, b, c}) == 3: 
                if a in d and b in d and c in d:
                    ans.append(x)

            elif len({a, b, c}) == 2: 
                if a == b:
                    if a in d and c in d and d[a] > 1:
                        ans.append(x)
                elif b == c:
                    if b in d and a in d and d[b] > 1:
                        ans.append(x)
                else:
                    if c in d and b in d and d[c] > 1:
                        ans.append(x)
						
            else: #if none unique
                if a in d and d[a] > 2:
                    ans.append(x)
                
        return ans