from collections import deque

def is_valid_state(missionaries, cannibals):
    if missionaries < 0 or cannibals < 0 or missionaries > 3 or cannibals > 3:
        return False
    if missionaries > 0 and missionaries < cannibals:
        return False
    return True

def is_goal_state(state):
    return state == (0, 0, 1)

def missionaries_cannibals():
    start_state = (3, 3, 0)  
    goal_state = (0, 0, 1)   
    
    moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]
    
    queue = deque([(start_state, [])])  
    
    visited = set()
    
    while queue:
        current_state, path = queue.popleft()
        missionaries_left, cannibals_left, boat_on_left = current_state
        
        if is_goal_state(current_state):
            return path + [current_state]
     
        visited.add(current_state)
        
   
        if boat_on_left == 0: 
            for move in moves:
                new_missionaries_left = missionaries_left - move[0]
                new_cannibals_left = cannibals_left - move[1]
                new_state = (new_missionaries_left, new_cannibals_left, 1)  
                
                if is_valid_state(new_missionaries_left, new_cannibals_left) and \
                   is_valid_state(3 - new_missionaries_left, 3 - new_cannibals_left) and \
                   new_state not in visited:
                    queue.append((new_state, path + [current_state]))
        
        else:  
            for move in moves:
                new_missionaries_left = missionaries_left + move[0]
                new_cannibals_left = cannibals_left + move[1]
                new_state = (new_missionaries_left, new_cannibals_left, 0)  
                
                if is_valid_state(new_missionaries_left, new_cannibals_left) and \
                   is_valid_state(3 - new_missionaries_left, 3 - new_cannibals_left) and \
                   new_state not in visited:
                    queue.append((new_state, path + [current_state]))
    
    return None 

def print_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        for state in solution:
            missionaries_left, cannibals_left, boat_on_left = state
            missionaries_right = 3 - missionaries_left
            cannibals_right = 3 - cannibals_left
            boat_position = "left" if boat_on_left == 0 else "right"
            print(f"Left bank: {missionaries_left}M {cannibals_left}C | "
                  f"Boat: {boat_position} | "
                  f"Right bank: {missionaries_right}M {cannibals_right}C")
        print("Solution found!")

solution = missionaries_cannibals()
print_solution(solution)