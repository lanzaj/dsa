class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        if n == 1:
            return True
        patate = {}
        for head, tail in edges:
            if head not in patate:
                patate[head] = set()
            patate[head].add(tail)
            if tail not in patate:
                patate[tail] = set()
            patate[tail].add(head)

        visited = set()
        def dfs(node, last):
            visited.add(node)
            for m in patate[node]:
                if m == last:
                    continue
                if m in visited:
                    return False
                res = dfs(m, node)
                if res == False:
                    return False
            return True


        return dfs(0, -1) and len(visited) == n