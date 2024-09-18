from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque([(0, 0, 0)]) 
    
    while queue:
        jug1, jug2, steps = queue.popleft()

        if jug1 == target or jug2 == target:
            print(f"Final state: ({jug1}, {jug2})")
            print(f"Number of steps taken: {steps}")
            return

        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        queue.append((jug1_capacity, jug2, steps + 1))
        
        queue.append((jug1, jug2_capacity, steps + 1))
        
        queue.append((0, jug2, steps + 1))
      
        queue.append((jug1, 0, steps + 1))
        
        pour_to_jug2 = min(jug1, jug2_capacity - jug2)
        queue.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2, steps + 1))
        
        pour_to_jug1 = min(jug2, jug1_capacity - jug1)
        queue.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1, steps + 1))

    print("No solution exists")

def main():
    m = int(input("Enter the capacity of the first jug: "))
    n = int(input("Enter the capacity of the second jug: "))
    d = int(input("Enter the desired amount of water: "))
    
    water_jug_problem(m, n, d)

if __name__ == "__main__":
    main()
