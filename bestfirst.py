import queue

def shortest_path(graph, start, end, heuristic):
  
    cost = {node: float('inf') for node in graph}
    cost[start] = 0


    priority_queue = queue.PriorityQueue()
    priority_queue.put((heuristic[start], 0, start))

    parent = {node: None for node in graph}

    while not priority_queue.empty():
 
        _, cost, node = priority_queue.get()
        if cost < cost[node]:
            cost[node] = cost
            for neighbor in graph[node]:
                new_cost = cost[node] + 1
                if new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost
                    priority = new_cost + heuristic[neighbor]
                    priority_queue.put((priority, new_cost, neighbor))
                    parent[neighbor] = node

    path = []
    while end:
        path.append(end)
        end = parent[end]
    path.reverse()

    return path


num_nodes = int(input("Enter the number of nodes: "))
graph = {}
for i in range(1, num_nodes+1):
    graph[i] = set()
    num_neighbors = int(input(f"Enter the number of neighbors of node {i}: "))
    for j in range(num_neighbors):
        neighbor = int(input(f"Enter the neighbor of node {i}: "))
        graph[i].add(neighbor)


heuristic = {}
for i in range(1, num_nodes+1):
    heuristic[i] = int(input(f"Enter the heuristic value for node {i}: "))


start = int(input("Enter the starting node: "))
end = int(input("Enter the ending node: "))


path = shortest_path(graph, start, end, heuristic)

# Print the shortest path
print("Shortest path:", path)
