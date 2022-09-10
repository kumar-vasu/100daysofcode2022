import math
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        a_list = {}
        
        for i in range(len(bombs)):
            a_list[i] = []
            for j in range(len(bombs)):
                
                if i == j:
                    continue
                
                if math.sqrt((bombs[i][1] - bombs[j][1])**2 + (bombs[i][0] - bombs[j][0])**2) <= bombs[i][2]:
                    a_list[i].append(j)
                        
        max_ = 0
        for i in range(len(bombs)):
            curr_blasts = 1
            curr_bomb = bombs[i]
            queue = [i]
            blasted = set([i])
            while len(queue) > 0:
                count = len(queue)
                for j in range(count):
                    curr = queue.pop(0)
                    for adj in a_list[curr]:
                        if adj not in blasted:
                            curr_blasts += 1
                            queue.append(adj)
                            blasted.add(adj)
            max_ = max(max_, curr_blasts)
        
        return max_