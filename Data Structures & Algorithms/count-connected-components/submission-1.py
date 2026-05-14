class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        self.components = n

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self, x: int) -> int:
        p = self.parent[x]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, x:int, y:int) -> bool:
        p1, p2 = self.find(x), self.find(y)
        if p1 == p2:
            return False
        if self.rank[p1] < self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p1] += 1
        self.components -= 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for x, y in edges:
            uf.union(x, y)
        return uf.components
        