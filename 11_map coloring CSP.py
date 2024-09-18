
def is_valid(node, color, assignment, neighbors):
    for neighbor in neighbors[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment, nodes, colors, neighbors):
    if len(assignment) == len(nodes):
        return assignment
    
    unassigned_nodes = [node for node in nodes if node not in assignment]
    node = unassigned_nodes[0]
    
    for color in colors:
        if is_valid(node, color, assignment, neighbors):
            assignment[node] = color 
            result = backtrack(assignment, nodes, colors, neighbors) 
            if result:
                return result
            assignment.pop(node)
    
    return None  
def map_coloring_csp(nodes, colors, neighbors):
    assignment = {}  
    return backtrack(assignment, nodes, colors, neighbors)

nodes = ['Western Australia', 'Northern Territory', 'South Australia', 
         'Queensland', 'New South Wales', 'Victoria', 'Tasmania']

neighbors = {
    'Western Australia': ['Northern Territory', 'South Australia'],
    'Northern Territory': ['Western Australia', 'South Australia', 'Queensland'],
    'South Australia': ['Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Victoria'],
    'Queensland': ['Northern Territory', 'South Australia', 'New South Wales'],
    'New South Wales': ['Queensland', 'South Australia', 'Victoria'],
    'Victoria': ['South Australia', 'New South Wales'],
    'Tasmania': []  
}

colors = ['Red', 'Green', 'Blue']


solution = map_coloring_csp(nodes, colors, neighbors)

if solution:
    print("Solution found:")
    for node, color in solution.items():
        print(f"{node}: {color}")
else:
    print("No solution found.")