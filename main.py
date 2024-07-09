def longest_path(graph: list) -> int:
    n = len(graph)
    
 
    def topological_sort():
        visited = [False] * n
        stack = []
        
        def dfs(node):
            visited[node] = True
            for neighbor, _ in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            stack.append(node)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
        
        return stack[::-1]
    

    def calculate_longest_path(topo_order):
        dist = [-float('inf')] * n
        for node in topo_order:
            if dist[node] == -float('inf'):
                dist[node] = 0
            for neighbor, weight in graph[node]:
                if dist[neighbor] < dist[node] + weight:
                    dist[neighbor] = dist[node] + weight
        
        return max(dist)

    topo_order = topological_sort()
    

    return calculate_longest_path(topo_order)


if __name__ == "__main__":
    graph = [
        [(1, 3), (2, 2)],
        [(3, 4)],
        [(3, 1)],
        []
    ]
    print(longest_path(graph))  
