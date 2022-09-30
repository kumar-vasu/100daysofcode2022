class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        def imp(emp, sub):
            sumi = 0
            for ele in sub:
                sumi += hashmap[ele].importance+imp(hashmap[ele], hashmap[ele].subordinates)
            return sumi
        hashmap = {}
        
        for emp in employees:
            hashmap[emp.id] = emp
        return hashmap[id].importance+imp(hashmap[id], hashmap[id].subordinates)