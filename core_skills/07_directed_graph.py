# Implementation of a Directed Graph (using an Adjacency List in this case) in Python
class Graph:
    
    def __init__(self):
        self.adjacency_list = {} # src -> set() of neighbors

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjacency_list:
            self.adjacency_list[src] = set()
        if dst not in self.adjacency_list:
            self.adjacency_list[dst] = set()
        self.adjacency_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjacency_list or dst not in self.adjacency_list[src]:
            return False
        self.adjacency_list[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        queue = deque([src])
        while queue:
            curr = queue.popleft()
            if curr == dst:
                return True
            visited.add(curr)
            for neighbor in self.adjacency_list.get(curr, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return False

    # Alternatively, use DFS for hasPath
    def hasPathDFS(self, src: int, dst: int) -> bool:
        visited = set()
        return self.dfs(src, dst, visited)
    
    # Helper function needed for DFS recursion
    def dfs(self, src, dst, visited):
        if src == dst:
            return True
        visited.add(src)
        for neighbor in self.adjacency_list.get(src, set()):
            if neighbor not in visited:
                if self.dfs(neighbor, dst, visited):
                    return True
        return False
