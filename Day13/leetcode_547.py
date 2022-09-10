class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        adj_list = {}
        for i in range(len(isConnected)):
            adj_list[i] = []
            
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i == j:
                    continue
                
                if isConnected[i][j] == 1:
                    adj_list[i].append(j)
        
        del isConnected
        
        visited = set()
        province = 0
        for i in adj_list:
            if i in visited:
                continue
            queue = [i]
            province += 1
            while len(queue) > 0:
                curr_len = len(queue)
                for j in range(curr_len):
                    curr = queue.pop(0)
                    for adj in adj_list[curr]:
                        if adj not in visited and adj not in queue:
                            queue.append(adj)
                    visited.add(curr)
        return province