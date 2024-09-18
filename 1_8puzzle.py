from collections import deque

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

print("Enter the initial state of the 8 puzzle (use 0 for the blank tile):")
initial_state = []
for i in range(3):
    row = list(map(int, input(f"Row {i + 1} (3 numbers separated by space): ").split()))
    initial_state.append(row)

queue = deque([(initial_state, [])])
visited = set()

while queue:
    state, path = queue.popleft()

    if state == goal_state:
        print("\nSolution:")
        for i, step in enumerate(path + [state]):
            print(f"Step {i + 1}:")
            for row in step:
                print(row)
            print()
        break

    if tuple(map(tuple, state)) in visited:
        continue

    visited.add(tuple(map(tuple, state)))

    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)

    moves = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    for new_x, new_y in moves:
        if 0 <= new_x < 3 and 0 <= new_y < 3:  
            new_state = [row[:] for row in state]  
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]  
            queue.append((new_state, path + [state]))