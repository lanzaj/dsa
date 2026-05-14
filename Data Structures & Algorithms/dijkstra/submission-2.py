class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for source, dest, weight in edges:
            adj[source].append([weight, dest])
        
        print(adj)
        ret = {}
        min_heap = [[0, src]]

        while min_heap:
            w, s = heapq.heappop(min_heap)

            if s in ret:
                continue

            ret[s] = w
            print(s)
            for w1, d1 in adj[s]:
                if d1 not in ret:
                    heapq.heappush(min_heap, [w1 + w, d1])
        for i in range(n):
            if i not in ret:
                ret[i] = -1
        return ret