class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        self.disjoint()
        for i in equations:
            if i[1]+i[2]=="==":
                self.union(i[0],i[3])
        for i in equations:
            if i[1]+i[2]=="!=" and not self.verify(i[0],i[1]+i[2],i[3]):
                return False
            else:
                continue
        return True
    def verify(self,a,sign,b):
        p1=self.find(ord(a)-97)
        p2=self.find(ord(b)-97)
        if sign=="!=":
            if p1==p2:
                return False
        elif sign=="==":
            if p1!=p2:
                return False
        return True
    def disjoint(self):
        self.parent=[i for i in range(26)]
        self.rank=[0 for i in range(26)]
    def find(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.find(self.parent[node])
        return self.parent[node]
    def union(self,a,b):
        p1=self.find(ord(a)-97)
        p2=self.find(ord(b)-97)
        if self.rank[p1]>self.rank[p2]:
            self.parent[p2]=p1
        elif self.rank[p2]>self.rank[p1]:
            self.parent[p1]=p2
        else:
            self.parent[p2]=p1
            self.rank[p1]+=1