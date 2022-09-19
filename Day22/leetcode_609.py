class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path_dict = {}
        for i in range(len(paths)):
            paths[i] = paths[i].split(" ")
            for j in range(len(paths[i])):
                if j ==0 :
                    paths[i][j] = paths[i][j].split("/")
                else:
                    paths[i][j] = paths[i][j][:-1]
                    paths[i][j] = paths[i][j].split("(")
                    if paths[i][j][-1] not in path_dict:
                        path_dict[paths[i][j][-1]] = [paths[i][0] + [paths[i][j][0]]]
                    else:
                        path_dict[paths[i][j][-1]].append(paths[i][0] + [paths[i][j][0]])
        res = []
        for i in path_dict:
            if len(path_dict[i]) > 1:
                res.append(["/".join(j) for j in path_dict[i]])
        return res