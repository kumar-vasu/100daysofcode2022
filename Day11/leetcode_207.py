class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency_list = {}
        for i in range(numCourses):
            adjacency_list[i] = set()
        
        zero_in = set()
        for i in range(numCourses):
            zero_in.add(i)
        
        for i in prerequisites:
            adjacency_list[i[0]].add(i[1])
            if i[0] in zero_in:
                zero_in.remove(i[0])
            
        zero_list = list(zero_in)
        traversed = set()
        while len(zero_list) != 0:
            curr = zero_list.pop()
            traversed.add(curr)
            for i in adjacency_list:
                if curr in adjacency_list[i]:
                    adjacency_list[i].remove(curr)
                    if len(adjacency_list[i]) == 0:
                        zero_list.append(i)
        if len(traversed) == numCourses:
            return True
        else:
            return False