class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # key: src      value: min_heap of (weight, destination)
        map_dict = {i: [] for i in range(n)}
        for edge in edges:
            if edge[0] not in map_dict:
                map_dict[edge[0]] = [(edge[2], edge[1])]
            else:
                map_dict[edge[0]].append((edge[2], edge[1]))
        
        print(map_dict)
          
        # set of visited nodes
        node_visited = set()
        # value to return
        ret = {}
        ret[src] = 0
        # dijkstra minheap
        min_heap = []
        for edge in map_dict[src]:
            heapq.heappush(min_heap, edge)
            node_visited.add(src)

        while min_heap:
            len, node_number = heapq.heappop(min_heap)
            if node_number in node_visited:
                continue
            if node_number not in node_visited:
                node_visited.add(node_number)
                ret[node_number] = len

            for edge in map_dict[node_number]:
                heapq.heappush(min_heap, (len + edge[0], edge[1]))

        return ret