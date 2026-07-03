class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        visited = [False]*n 

        for key, val in edges:
            if visited[key] and visited[val]:
                return False
            
            visited[key] = True
            visited[val] = True
        
        return True


        