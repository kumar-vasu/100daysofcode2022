class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        map_ = {}
        for i in range(len(pieces)):
            map_[pieces[i][0]] = pieces[i]
            
        
        i = 0    
        r =len(arr)
        while i<r:
            if arr[i] not in map_.keys():
                return False
            
            else:
                lis = map_[arr[i]]
                
                for j in range(len(lis)):
                    
                    if lis[j] != arr[i]:
                        return False
                    i += 1
       
        return True
