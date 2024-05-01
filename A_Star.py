import numpy as np
import queue 

n = int(input("Enter number of nodes: "))
edges = int(input("Enter number of edges: "))
adj_martix = np.zeros((n, n), dtype=int)
heuristic = np.zeros(n, dtype=int)

def add_edges():
    for i in range(edges):
        i, j, weight = map(int, input("Enter First and Second Node followed by weight: ").split())
        adj_martix[i][j] = weight
        adj_martix[j][i] = weight

def add_heuristic():
    for i in range(n):
        val = int(input(f"Enter heuristic value for node {i}: "))
        heuristic[i] = val

add_edges()
add_heuristic()

start = int(input("Enter starting node: "))
end = int(input("Enter Goal node: "))


def solve_aStar():
    open = queue.PriorityQueue()
    open.put((0, start)) #We're putting pairs in open, pair of f(x) and the node
    came_from = {start: None}
    cost_so_far = {start: 0}
    closed = set() #We're using a set here beacause the lookup time will be O(1) instead of O(n) in case of a list
    while not open.empty():
        current_cost, current_node = open.get()
        closed.add(current_node)
        print("Open Nodes: ", open.queue)
        print("Closed Nodes: ", closed)
        if current_node == end:
            print("Reached")
            break
        for next in range(n):
            if adj_martix[current_node][next] > 1 and next not in closed:
                new_cost = cost_so_far[current_node] + adj_martix[current_node][next]
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic[next]
                    open.put((priority, next))
                    came_from[next] = current_node
    return came_from, cost_so_far

came_from, cost_so_far = solve_aStar()




