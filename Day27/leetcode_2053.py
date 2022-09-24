import copy
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        res = copy.deepcopy(arr)
        seen = set()
        for i in res:
            #print(i)
            if i in seen:
                while True:
                    try:
                        arr.remove(i)
                    except:
                        break
            else:
                seen.add(i)
        #print(arr)
        if len(arr) >= k:
            return arr[k-1]
        else:
            return ""