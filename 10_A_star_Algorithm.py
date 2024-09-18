from queue import PriorityQueue

def heuristic(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def a_star(graph, start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start)) 
    
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)
    
    visited = set()
    
    while not open_set.empty():
        current = open_set.get()[1] 
        visited.add(current)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for neighbor in graph[current]:
            if neighbor in visited:
                continue
            
            tentative_g_score = g_score[current] + graph[current][neighbor]
            
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                open_set.put((f_score[neighbor], neighbor))
    
    return None  
graph = {
    (0, 0): {(0, 1): 1.5, (1, 0): 2},
    (0, 1): {(0, 0): 1.5, (1, 1): 2},
    (1, 0): {(0, 0): 2, (1, 1): 2.5},
    (1, 1): {(1, 0): 2.5, (0, 1): 2}
}

start = (0, 0) 
goal = (1, 1) 

path = a_star(graph, start, goal)

if path:
    print(f"Path found: {path}")
else:
    print("No path found.")