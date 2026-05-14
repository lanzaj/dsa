class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        if n == 1:
            return True
        adj = {}
        for head, tail in edges:
            if head not in adj:
                adj[head] = set()
            adj[head].add(tail)
            if tail not in adj:
                adj[tail] = set()
            adj[tail].add(head)

        visited = set()
        def dfs(node, last):
            if node in visited:
                return False
            visited.add(node)
            for m in adj[node]:
                if m == last:
                    continue
                if not dfs(m, node):
                    return False
            return True


        return dfs(0, -1) and len(visited) == n