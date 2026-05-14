class Graph:
    
    def __init__(self):
        self.graph = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = []
        if dst not in self.graph:
            self.graph[dst] = []
        if dst not in self.graph[src]:
            self.graph[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph or dst not in self.graph:
            return False
        if dst in self.graph[src]:
            self.graph[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()

        def bfs(src: int, dst: int) -> bool:
            if src == dst:
                return True
            if src in visited:
                return False
            visited.add(src)
            for neighbour in self.graph[src]:
                if bfs(neighbour, dst):
                    return True
            return False
        
        return bfs(src, dst)

