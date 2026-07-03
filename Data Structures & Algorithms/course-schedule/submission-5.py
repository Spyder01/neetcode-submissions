class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:

        edges = {}

        for k, v in prerequisites:
            if k == v:
                return False
                
            if k not in edges:
                edges[k] = []

            edges[k].append(v)

        visited = [False for _ in range(n)]
        cyclic = False

        print(edges)
        def dfs(index):
            nonlocal cyclic

            if visited[index]:
                cyclic = True
                return
            
            if index not in edges:
                return
            visited[index] = True

            for vertex in edges.get(index):
                dfs(vertex)
            
            visited[index] = False
        
        for i in range(n):
            dfs(i)
        
        return not cyclic



        