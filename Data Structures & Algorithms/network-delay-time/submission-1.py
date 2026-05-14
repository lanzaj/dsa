class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append([w, v])
        
        time = 0
        signalSpread = [[0, k]]
        visited = set()
        while signalSpread:
            weight, src = heapq.heappop(signalSpread)

            if src in visited:
                continue
            visited.add(src)
            time = max(time, weight)
            for w2, src2 in adj[src]:
                if src2 not in visited:
                    heapq.heappush(signalSpread, [weight + w2, src2])
        return time if len(visited) == n else -1