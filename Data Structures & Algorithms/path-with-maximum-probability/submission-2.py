class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([succProb[i], dst])
            adj[dst].append([succProb[i], src])
        
        minHeap = [[-1, start_node]]
        visited = set()
        while minHeap:
            p, n = heapq.heappop(minHeap)

            if n in visited:
                continue

            visited.add(n)
            if n == end_node:
                return -p
            for p2, n2 in adj[n]:
                if n2 not in visited:
                    heapq.heappush(minHeap, [p * p2, n2])
                
        return 0
