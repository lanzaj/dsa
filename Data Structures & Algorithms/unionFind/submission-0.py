class UnionFind:
    
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        self.num_components = n

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
        
    def find(self, x: int) -> int:
        p = self.par[x]
        while self.par[p] != p:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        r1 = self.find(x)
        r2 = self.find(y)

        return r1 == r2


    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y):
            return False
        
        if self.rank[x] < self.rank[y]:
            self.par[y] = x
        elif self.rank[x] > self.rank[y]:
            self.par[x] = y
        else:
            self.par[x] = y
            self.rank[x] += 1
        self.num_components -= 1
        return True
        

    def getNumComponents(self) -> int:
        return self.num_components

