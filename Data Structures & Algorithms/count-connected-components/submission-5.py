class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edges_ = {}

        for k, v in edges:
            if k not in edges_:
                edges_[k] = []
            
            edges_[k].append(v)

            if v not in edges_:
                edges_[v] = []
            
            edges_[v].append(k)

        print(edges_)
        count = 0
        visited = [False for _ in range(n)]

        def dfs(i):
            if i not in edges_:
                visited[i] = True
                return
            

            visited[i] = True
            taken = True 
            for node in edges_.get(i):
                if visited[node]:
                    continue

                dfs(node)

            return taken 

        for i in range(n):
            if visited[i]:
                continue
            
            dfs(i)
            count += 1
        
        return count

        